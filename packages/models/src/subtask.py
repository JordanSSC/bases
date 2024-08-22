from dataclasses import dataclass

from packages.models.src.priority import Priority
from packages.models.src.status import Status
from packages.models.src.task import Task


@dataclass(frozen=True)
class Subtask:
    id: int
    title: str
    currentStatus: Status
    currentPriority: Priority
    mainTask: Task