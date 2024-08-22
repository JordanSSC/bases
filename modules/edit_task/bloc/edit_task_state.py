from enum import Enum

from packages.models import Priority, Status, Task


class EditTaskStatus(Enum):
    initial = "initial"
    loading = "loading"
    success = "success"
    failure = "failure"


class EditTaskState:
    def __init__(self, *, initialTask: Task) -> None:
        self.initialTask = initialTask
        self.title = initialTask.title
        self.description = initialTask.description
        self.currentStatus = initialTask.currentStatus
        self.currentPriority = initialTask.currentPriority
        self.status = EditTaskStatus.initial
        self.dueDate = initialTask.dueDate
