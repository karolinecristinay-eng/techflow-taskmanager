"""
Testes de integração da API REST (camada Flask), usando o cliente de
testes do próprio Flask (sem precisar subir um servidor real).
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import create_app  # noqa: E402
from models import TaskRepository  # noqa: E402


@pytest.fixture
def repo():
    return TaskRepository()


@pytest.fixture
def client(repo):
    app = create_app(repo=repo)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200


def test_list_tasks_returns_seed_data(client, repo):
    repo.create("Modelar diagrama de casos de uso", status="done", priority="high")
    repo.create("Configurar pipeline de CI no GitHub Actions", status="in_progress", priority="critical")
    response = client.get("/api/tasks")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2


def test_create_task_via_api(client):
    response = client.post("/api/tasks", json={
        "title": "Nova tarefa via API",
        "priority": "critical",
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Nova tarefa via API"
    assert data["priority"] == "critical"


def test_create_task_without_title_returns_400(client):
    response = client.post("/api/tasks", json={"title": ""})
    assert response.status_code == 400


def test_create_task_with_invalid_json_returns_400(client):
    response = client.post(
        "/api/tasks",
        data="{ invalid json }",
        content_type="application/json",
    )
    assert response.status_code == 400
    assert response.get_json()["error"] == "JSON inválido."


def test_get_missing_task_returns_404(client):
    response = client.get("/api/tasks/99999")
    assert response.status_code == 404


def test_update_task_via_api(client):
    created = client.post("/api/tasks", json={"title": "Para atualizar"}).get_json()
    response = client.put(f"/api/tasks/{created['id']}", json={"status": "done"})
    assert response.status_code == 200
    assert response.get_json()["status"] == "done"


def test_delete_task_via_api(client):
    created = client.post("/api/tasks", json={"title": "Para deletar"}).get_json()
    response = client.delete(f"/api/tasks/{created['id']}")
    assert response.status_code == 204
    assert client.get(f"/api/tasks/{created['id']}").status_code == 404
