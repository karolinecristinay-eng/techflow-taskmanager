"""
Aplicação web (Flask) do sistema de gerenciamento de tarefas da TechFlow
Solutions, desenvolvido para o cliente fictício (startup de logística).

Expõe:
  - Uma API REST (/api/tasks) para operações CRUD.
  - Uma interface HTML simples (/) para uso e demonstração no vídeo pitch.
"""

from flask import Flask, jsonify, request, render_template

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
        data = request.get_json(silent=True) or request.form
        try:
            task = app.repo.create(
                title=data.get("title"),
                description=data.get("description", ""),
                status=data.get("status", "todo"),
                priority=data.get("priority", "medium"),
            )
        except ValidationError as e:
            return jsonify({"error": str(e)}), 400
        return jsonify(task.to_dict()), 201

    @app.get("/api/tasks/<int:task_id>")
    def get_task(task_id):
        try:
            task = app.repo.get(task_id)
        except TaskNotFoundError as e:
            return jsonify({"error": str(e)}), 404
        return jsonify(task.to_dict())

    @app.put("/api/tasks/<int:task_id>")
    def update_task(task_id):
        data = request.get_json(silent=True) or request.form
        try:
            task = app.repo.update(task_id, **data)
        except TaskNotFoundError as e:
            return jsonify({"error": str(e)}), 404
        except ValidationError as e:
            return jsonify({"error": str(e)}), 400
        return jsonify(task.to_dict())

    @app.delete("/api/tasks/<int:task_id>")
    def delete_task(task_id):
        try:
            app.repo.delete(task_id)
        except TaskNotFoundError as e:
            return jsonify({"error": str(e)}), 404
        return "", 204

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
