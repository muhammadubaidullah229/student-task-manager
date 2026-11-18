"""Student Task Manager — console menu.

Run with:  python main.py
"""

from task_manager import TaskManager


def show_menu():
    print("\n--- Student Task Manager ---")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def display_tasks(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet. Add your first task!")
        return
    for task in tasks:
        status = "Done" if task.completed else "Pending"
        print(f"{task.id}. [{status}] {task.title}")


def main():
    manager = TaskManager()
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            title = input("Enter task title: ")
            try:
                task = manager.add_task(title)
                print(f"Task added: {task.title}")
            except ValueError as e:
                print(f"Could not add task: {e}")
        elif choice == "2":
            display_tasks(manager)
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: "))
                if manager.complete_task(task_id):
                    print(f"Task {task_id} marked as completed.")
                else:
                    print(f"No task found with ID {task_id}.")
            except ValueError:
                print("Please enter a valid task ID (a positive number).")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                if manager.delete_task(task_id):
                    print(f"Task {task_id} deleted.")
                else:
                    print(f"No task found with ID {task_id}.")
            except ValueError:
                print("Please enter a valid task ID (a positive number).")
        elif choice == "5":
            print("Goodbye! Your tasks are saved.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
