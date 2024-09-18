class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def update(self, title=None, description=None, deadline=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if deadline:
            self.deadline = deadline

    def __str__(self):
        status = 'Completed' if self.completed else 'Pending'
        return f'{self.title} - {self.description} (Due: {self.deadline}) - {status}'

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, deadline):
        task = Task(title, description, deadline)
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f'{i}. {task}')

    def update_task(self, task_id, title=None, description=None, deadline=None):
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id].update(title, description, deadline)
        else:
            print("Invalid task ID")

    def delete_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            del self.tasks[task_id]
        else:
            print("Invalid task ID")

    def mark_task_complete(self, task_id):
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id].mark_complete()
        else:
            print("Invalid task ID")

# Example usage
if __name__ == "__main__":
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Mark Task Complete\n6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Task Title: ")
            description = input("Task Description: ")
            deadline = input("Task Deadline: ")
            todo_list.add_task(title, description, deadline)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks()
            task_id = int(input("Enter task number to update: ")) - 1
            title = input("New Title (leave blank to skip): ")
            description = input("New Description (leave blank to skip): ")
            deadline = input("New Deadline (leave blank to skip): ")
            todo_list.update_task(task_id, title or None, description or None, deadline or None)
        elif choice == "4":
            todo_list.view_tasks()
            task_id = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(task_id)
        elif choice == "5":
            todo_list.view_tasks()
            task_id = int(input("Enter task number to mark complete: ")) - 1
            todo_list.mark_task_complete(task_id)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
