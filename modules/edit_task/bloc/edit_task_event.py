from abc import ABC
from datetime import date
from packages.models.src.user import User
from packages.models.src.status import Status
from packages.models.src.priority import Priority

class EditTaskEvent(ABC):
    pass

class EditTaskTitleChanged(EditTaskEvent):
    def __init__(self, *, title: str) -> None:
        self.title = title

class EditTaskDescriptionChanged(EditTaskEvent):
    def __init__(self, *, description: str) -> None:
        self.description = description

class EditTaskDueDateChanged(EditTaskEvent):
    def __init__(self, *, dueDate: date) -> None:
        self.dueDate = dueDate

class EditTaskUserChanged(EditTaskEvent):
    def __init__(self, *, user: User) -> None:
        self.user = user

class EditTaskCurrentStatusChanged(EditTaskEvent):
    def __init__(self, *, currentStatus: Status) -> None:
        self.currentStatus = currentStatus

class EditTaskCurrentPriorityChanged(EditTaskEvent):
    def __init__(self, *, currentPriority: Priority) -> None:
        self.currentPriority = currentPriority

class EditTaskSubmitted:
    def __init__(self) -> None:
        pass

