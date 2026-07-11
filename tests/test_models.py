"""
Testes unitários do repositório de tarefas.

Estes testes são executados automaticamente pelo pipeline de Integração
Contínua (GitHub Actions) configurado em .github/workflows/ci.yml,
garantindo o controle de qualidade do código a cada push/pull request.
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from models import TaskRepository, ValidationError, TaskNotFoundError


@pytest.fixture
def repo():
    return TaskRepository()


def test_create_task_success(repo):
    task = repo.create(title="Escrever README", priority="high")
    assert task.id == 1
    assert task.title == "Escrever README"
    assert task.status == "todo"
    assert task.priority == "high"


def test_create_task_without_title_raises(repo):
    with pytest.raises(ValidationError):
        repo.create(title="   ")


def test_create_task_invalid_status_raises(repo):
    with pytest.raises(ValidationError):
        repo.create(title="Tarefa X", status="invalido")


def test_create_task_invalid_priority_raises(repo):
    with pytest.raises(ValidationError):
        repo.create(title="Tarefa X", priority="urgentissimo")


def test_list_all_orders_by_priority(repo):
    repo.create(title="Baixa", priority="low")
    repo.create(title="Critica", priority="critical")
    repo.create(title="Media", priority="medium")

    ordered = repo.list_all()
    assert [t.priority for t in ordered] == ["critical", "medium", "low"]


def test_list_all_filters_by_status(repo):
    repo.create(title="A", status="todo")
    repo.create(title="B", status="done")

    done_tasks = repo.list_all(status="done")
    assert len(done_tasks) == 1
    assert done_tasks[0].title == "B"


def test_get_existing_task(repo):
    created = repo.create(title="Consultar")
    fetched = repo.get(created.id)
    assert fetched.id == created.id


def test_get_missing_task_raises(repo):
    with pytest.raises(TaskNotFoundError):
        repo.get(999)


def test_update_task_fields(repo):
    task = repo.create(title="Antigo título")
    updated = repo.update(task.id, title="Novo título", status="in_progress")
    assert updated.title == "Novo título"
    assert updated.status == "in_progress"


def test_update_task_empty_title_raises(repo):
    task = repo.create(title="Antigo título")
    with pytest.raises(ValidationError):
        repo.update(task.id, title="   ")


def test_update_missing_task_raises(repo):
    with pytest.raises(TaskNotFoundError):
        repo.update(999, title="qualquer")


def test_update_invalid_priority_raises(repo):
    task = repo.create(title="Tarefa")
    with pytest.raises(ValidationError):
        repo.update(task.id, priority="inexistente")


def test_delete_task(repo):
    task = repo.create(title="Removível")
    repo.delete(task.id)
    with pytest.raises(TaskNotFoundError):
        repo.get(task.id)


def test_delete_missing_task_raises(repo):
    with pytest.raises(TaskNotFoundError):
        repo.delete(999)
