from dataclasses import dataclass, field
from datetime import date

from packages.models.src.priority import Priority
from packages.models.src.status import Status
from packages.models.src.user import User

from typing import Optional

@dataclass(frozen=True)
class Task:
    id: int
    title: str
    description: str
    dueDate: date
    user: User
    currentStatus: Status = Status.PENDING
    currentPriority: Priority = Priority.PRIORITY_1