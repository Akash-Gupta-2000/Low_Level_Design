from task import TaskStatus

class Sprint:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def print_details(self):
        print(f"Sprint: {self.name}")
        for task in self.tasks:
            print(f"Task: {task.title}, Type: {task.task_type}, Status: {task.status}")

    def print_delayed_tasks(self):
        delayed_tasks = [task for task in self.tasks if task.status != TaskStatus.CLOSED]
        print("Delayed Tasks:")
        for task in delayed_tasks:
            print(f"Task: {task.title}, Status: {task.status}")

    def print_tasks_assigned_to_user(self, user):
        user_tasks = [task for task in self.tasks if user in task.assigned_to]
        print(f"Tasks assigned to {user}:")
        for task in user_tasks:
            print(f"Task: {task.title}, Type: {task.task_type}, Status: {task.status}")
