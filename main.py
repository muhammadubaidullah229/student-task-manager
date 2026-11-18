"""Student Task Manager — console menu.

Run with:  python main.py
"""

from task_manager import TaskManager


def show_menu():
    print("\n--- Student Task Manager ---")
    print("1. Add Task")
    print("2. Display Tasks")
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
        choice = input("Enter your choice (1, 2 or 5): ").strip()
        if choice == "1":
            title = input("Enter task title: ")
            try:
                task = manager.add_task(title)
                print(f"Task added: {task.title}")
            except ValueError as e:
                print(f"Could not add task: {e}")
        elif choice == "2":
            display_tasks(manager)
        elif choice == "5":
            print("Goodbye! Your tasks are saved.")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 5.")


if __name__ == "__main__":
    main()
