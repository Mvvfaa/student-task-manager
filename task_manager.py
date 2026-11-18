"""Student Task Manager - a simple console application."""


class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed


class TaskManager:
    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, title):
        task = Task(self._next_id, title)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def complete_task(self, task_id):
        raise NotImplementedError

    def delete_task(self, task_id):
        raise NotImplementedError

    def get_tasks(self):
        return list(self.tasks)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return
        print("\n--- Your Tasks ---")
        for t in self.tasks:
            status = "[x]" if t.completed else "[ ]"
            print(f"{t.id}. {status} {t.title}")

def main():
    manager = TaskManager()
    while True:
        print("\n=== Student Task Manager ===")
        print("1. Add task")
        print("2. Display tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task title: ")
            try:
                task = manager.add_task(title)
                print(f"Added task #{task.id}.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            manager.display_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Task ID to complete: "))
                manager.complete_task(task_id)
                print("Task marked as completed.")
            except ValueError as e:
                print(f"Error: {e}")
            except NotImplementedError:
                print("Not implemented yet.")
        elif choice == "4":
            try:
                task_id = int(input("Task ID to delete: "))
                manager.delete_task(task_id)
                print("Task deleted.")
            except ValueError as e:
                print(f"Error: {e}")
            except NotImplementedError:
                print("Not implemented yet.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()