from enum import Enum

class TaskType(Enum):
    BUG = "Bug"
    STORY = "Story"
    FEATURE = "Feature"

class TaskStatus(Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    CLOSED = "Closed"

class Task:
    def __init__(self, title, description, task_type, status):
        self.title = title
        self.description = description
        self.task_type = task_type
        self.status = status
        self.subtasks = []
        self.assigned_to = []

    def change_status(self, new_status):
        self.status = new_status

    def add_subtask(self, subtask):
        self.subtasks.append(subtask)

class Subtask(Task):
    def __init__(self, title, description, task_type, status):
        super().__init__(title, description, task_type, status)
