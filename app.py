"""
Aplicação web (Flask) do sistema de gerenciamento de tarefas da TechFlow
Solutions, desenvolvido para o cliente fictício (startup de logística).

Expõe:
  - Uma API REST (/api/tasks) para operações CRUD.
  - Uma interface HTML simples (/) para uso e demonstração no vídeo pitch.
"""

from flask import Flask, jsonify, request, render_template
from werkzeug.exceptions import BadRequest

from models import TaskRepository, ValidationError, TaskNotFoundError, VALID_PRIORITIES, VALID_STATUSES


def create_app(repo: TaskRepository | None = None) -> Flask:
    app = Flask(__name__)
    task_repo = repo if repo is not None else TaskRepository()

    if repo is None:
        # Dados de exemplo para já nascer com o sistema demonstrável.
        task_repo.create("Modelar diagrama de casos de uso", status="done", priority="high")
        task_repo.create("Configurar pipeline de CI no GitHub Actions", status="in_progress", priority="critical")
        task_repo.create("Implementar CRUD de tarefas", status="in_progress", priority="high")
        task_repo.create("Escrever documentação no README", status="todo", priority="medium")

    app.repo = task_repo

    def parse_request_data() -> dict:
        if request.is_json:
            return request.get_json()
        return request.form.to_dict()

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return jsonify({"error": str(error)}), 400

    @app.errorhandler(TaskNotFoundError)
    def handle_task_not_found(error):
        return jsonify({"error": str(error)}), 404

    @app.errorhandler(BadRequest)
    def handle_bad_request(error):
        return jsonify({"error": "JSON inválido."}), 400

    @app.get("/")
    def index():
        return render_template(
            "index.html",
            tasks=app.repo.list_all(),
            statuses=VALID_STATUSES,
            priorities=VALID_PRIORITIES,
        )

    @app.get("/api/tasks")
    def list_tasks():
        status = request.args.get("status")
        priority = request.args.get("priority")
        tasks = app.repo.list_all(status=status, priority=priority)
        return jsonify([t.to_dict() for t in tasks])

    @app.post("/api/tasks")
    def create_task():
        data = parse_request_data()
        task = app.repo.create(
            title=data.get("title"),
            description=data.get("description", ""),
            status=data.get("status", "todo"),
            priority=data.get("priority", "medium"),
        )
        return jsonify(task.to_dict()), 201

    @app.get("/api/tasks/<int:task_id>")
    def get_task(task_id):
        task = app.repo.get(task_id)
        return jsonify(task.to_dict())

    @app.put("/api/tasks/<int:task_id>")
    def update_task(task_id):
        data = parse_request_data()
        task = app.repo.update(task_id, **data)
        return jsonify(task.to_dict())

    @app.delete("/api/tasks/<int:task_id>")
    def delete_task(task_id):
        app.repo.delete(task_id)
        return "", 204

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
