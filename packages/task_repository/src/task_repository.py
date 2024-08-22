from datetime import date
from typing import List

from packages.models import Priority, Reminder, Status, Subtask, Task, User
from packages.task_api import TaskApi


class TaskRepository:
    def __init__(self, *, taskApi: TaskApi) -> None:
        self.taskApi = taskApi

    def getTasksForUser(self, *, user: User) -> List[Task]:
        self.taskApi.getTasksForUser(user=user)

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
        self.taskApi.saveTask(
            user=user,
            taskTitle=taskTitle,
            taskDescription=taskDescription,
            taskDate=taskDate,
            taskStatus=taskStatus,
            taskPriority=taskPriority,
        )

    def updateTask(self, *, task: Task) -> None:
        self.taskApi.updateTask(task=task)

    def deleteTask(self, *, task: Task) -> None:
        self.taskApi.deleteTask(task=task)

    def getSubtasksForTask(self, *, task: Task) -> List[Subtask]:
        self.taskApi.getSubtasksForTask(task=task)

    def saveSubtask(
        self,
        *,
        mainTask: Task,
        subtaskTitle: str,
        subtaskStatus: Status = Status.PENDING,
        subtaskPriority: Priority = Priority.PRIORITY_1
    ) -> None:
        self.taskApi.saveSubtask(
            mainTask=mainTask,
            subtaskTitle=subtaskTitle,
            subtaskStatus=subtaskStatus,
            subtaskPriority=subtaskPriority,
        )

    def updateSubtask(self, *, subtask: Subtask) -> None:
        self.taskApi.updateSubtask(subtask=subtask)

    def deleteSubtask(self, *, subtask: Subtask) -> None:
        self.taskApi.deleteSubtask(subtask=subtask)

    def getRemindersForTask(self, task: Task) -> List[Reminder]:
        self.taskApi.getRemindersForTask(task=task)

    def saveReminder(
        self, *, task: Task, reminderDescription: str, reminderDate: date
    ) -> None:
        self.taskApi.saveReminder(
            task=task,
            reminderDescription=reminderDescription,
            reminderDate=reminderDate,
        )

    def deleteReminder(self, *, reminder: Reminder) -> None:
        self.taskApi.deleteReminder(reminder=reminder)