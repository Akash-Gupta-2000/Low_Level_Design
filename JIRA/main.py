from task import Task, TaskType, TaskStatus
from sprint import Sprint
from user import User

def main():
    # Create users
    user1 = User("Akash")
    user2 = User("Abhishek")

    # Create tasks and subtasks
    task1 = Task("Task 1", "Description for Task 1", TaskType.BUG, TaskStatus.OPEN)
    subtask1 = Task("Subtask 1", "Description for Subtask 1", TaskType.STORY, TaskStatus.IN_PROGRESS)
    task2 = Task("Task 2", "Description for Task 2", TaskType.FEATURE, TaskStatus.OPEN)

    # Assign users to tasks
    task1.assigned_to = [user1]
    task2.assigned_to = [user2]

    # Create a sprint and add tasks
    sprint1 = Sprint("Sprint 1")
    sprint1.add_task(task1)
    sprint1.add_task(subtask1)
    sprint1.add_task(task2)

    # Print Sprint details, delayed tasks, and tasks assigned to users
    sprint1.print_details()
    sprint1.print_delayed_tasks()
    sprint1.print_tasks_assigned_to_user(user1)
    sprint1.print_tasks_assigned_to_user(user2)

if __name__ == "__main__":
    main()
