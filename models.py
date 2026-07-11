"""
Módulo de modelagem de dados do sistema de gerenciamento de tarefas.

Este módulo concentra a regra de negócio (camada de domínio), mantendo-a
isolada da camada web (Flask), o que facilita testes automatizados e
manutenção futura.
"""

from dataclasses import dataclass, field, asdict
from datetime import datetime
from itertools import count
from typing import Optional


# Status possíveis de uma tarefa, espelhando as colunas do quadro Kanban
# ("A Fazer", "Em Progresso", "Concluído") usado no GitHub Projects.
VALID_STATUSES = ("todo", "in_progress", "done")

# Níveis de prioridade. Este campo foi adicionado como parte da simulação
# de MUDANÇA DE ESCOPO do projeto (ver README.md, seção "Gestão de Mudanças"),
# atendendo ao pedido do cliente de "priorizar tarefas críticas".
VALID_PRIORITIES = ("low", "medium", "high", "critical")


@dataclass
class Task:
    """Representa uma tarefa dentro do sistema."""

    id: int
    title: str
    description: str = ""
    status: str = "todo"
    priority: str = "medium"
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    def to_dict(self) -> dict:
        return asdict(self)


class ValidationError(Exception):
    """Erro de validação de dados de entrada."""


class TaskNotFoundError(Exception):
    """Erro lançado quando uma tarefa não é encontrada pelo id informado."""


class TaskRepository:
    """
    Repositório em memória responsável pelas operações CRUD
    (Create, Read, Update, Delete) sobre as tarefas.

    Uma implementação em memória foi escolhida propositalmente para que o
    projeto seja simples de rodar e de testar (sem exigir um banco de
    dados externo), mantendo o foco da atividade nos conceitos de
    Engenharia de Software: versionamento, CI e gestão ágil.
    """

    def __init__(self):
        self._tasks: dict[int, Task] = {}
        self._id_counter = count(1)

    def create(self, title: str, description: str = "", status: str = "todo",
               priority: str = "medium") -> Task:
        title = (title or "").strip()
        if not title:
            raise ValidationError("O campo 'title' é obrigatório.")
        if status not in VALID_STATUSES:
            raise ValidationError(f"Status inválido. Use um de: {VALID_STATUSES}")
        if priority not in VALID_PRIORITIES:
            raise ValidationError(f"Prioridade inválida. Use um de: {VALID_PRIORITIES}")

        task_id = next(self._id_counter)
        task = Task(id=task_id, title=title, description=description,
                    status=status, priority=priority)
        self._tasks[task_id] = task
        return task

    def list_all(self, status: Optional[str] = None,
                 priority: Optional[str] = None) -> list[Task]:
        tasks = list(self._tasks.values())
        if status:
            tasks = [t for t in tasks if t.status == status]
        if priority:
            tasks = [t for t in tasks if t.priority == priority]
        # Tarefas críticas/altas aparecem primeiro, facilitando o
        # acompanhamento do fluxo de trabalho em tempo real pedido pelo cliente.
        order = {p: i for i, p in enumerate(reversed(VALID_PRIORITIES))}
        return sorted(tasks, key=lambda t: order[t.priority])

    def get(self, task_id: int) -> Task:
        task = self._tasks.get(task_id)
        if not task:
            raise TaskNotFoundError(f"Tarefa {task_id} não encontrada.")
        return task

    def update(self, task_id: int, **fields) -> Task:
        task = self.get(task_id)
        if "status" in fields and fields["status"] not in VALID_STATUSES:
            raise ValidationError(f"Status inválido. Use um de: {VALID_STATUSES}")
        if "priority" in fields and fields["priority"] not in VALID_PRIORITIES:
            raise ValidationError(f"Prioridade inválida. Use um de: {VALID_PRIORITIES}")
        if "title" in fields:
            title = (fields["title"] or "").strip()
            if not title:
                raise ValidationError("O campo 'title' é obrigatório.")
            fields["title"] = title

        for key in ("title", "description", "status", "priority"):
            if key in fields and fields[key] is not None:
                setattr(task, key, fields[key])
        task.updated_at = datetime.utcnow().isoformat()
        return task

    def delete(self, task_id: int) -> None:
        self.get(task_id)  # garante que existe, senão levanta TaskNotFoundError
        del self._tasks[task_id]
