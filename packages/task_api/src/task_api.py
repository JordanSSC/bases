from abc import ABC, abstractmethod
from datetime import date
from typing import List

from packages.models import Priority, Reminder, Status, Subtask, Task, User


class TaskApi(ABC):
    @abstractmethod
    def getTasksForUser(self, *, user: User) -> List[Task]:
        pass

    @abstractmethod
    def saveTask(
        self,
        *,
        user: User,
        taskTitle: str,
        taskDescription: str,
        taskDate: date,
        taskStatus: Status = Status.PENDING,
        taskPriority: Priority = Priority.PRIORITY_1
    ) -> None:
        pass

    @abstractmethod
    def updateTask(self, *, task: Task) -> None:
        pass

    @abstractmethod
    def deleteTask(self, *, task: Task) -> None:
        pass

    @abstractmethod
    def getSubtasksForTask(self, *, task: Task) -> List[Subtask]:
        pass

    @abstractmethod
    def saveSubtask(
        self,
        *,
        mainTask: Task,
        subtaskTitle: str,
        subtaskStatus: Status = Status.PENDING,
        subtaskPriority: Priority = Priority.PRIORITY_1
    ) -> None:
        pass

    @abstractmethod
    def updateSubtask(self, *, subtask: Subtask) -> None:
        pass

    @abstractmethod
    def deleteSubtask(self, *, subtask: Subtask) -> None:
        pass

    @abstractmethod
    def getRemindersForTask(self, task: Task) -> List[Reminder]:
        pass

    @abstractmethod
    def saveReminder(
        self, *, task: Task, reminderDescription: str, reminderDate: date
    ) -> None:
        pass

    @abstractmethod
    def deleteReminder(self, *, reminder: Reminder) -> None:
        pass