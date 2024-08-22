from dataclasses import dataclass
from datetime import date

from packages.models.src.task import Task


@dataclass(frozen=True)
class Reminder:
    id: int
    description: str
    reminderDate: date
    task: Task