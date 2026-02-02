"""
Main CLI interface for the Console Todo App.

This module contains the main application loop that provides a menu-driven
interface for users to interact with their todo tasks.
"""

from todo_manager import TodoManager


def main():
    """
    Main function to run the Console Todo App.

    Initializes the TodoManager and runs the menu-driven CLI loop.
    """
    print("Welcome to the Console Todo App!")
    print("Initializing application...")

    # Initialize the TodoManager
    manager = TodoManager()

    # Display a simple message indicating the app is ready
    print("TodoManager initialized successfully.")
    print("Application is ready. Use the CLI interface to manage your tasks.")

    while True:
        print("\nConsole Todo App Menu:")
        print("1. Add Task")
        print("2. View Task List")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark as Complete")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == '1':
            # Add Task
            title = input("Enter task title: ").strip()

            if not title:
                print("Error: Task title cannot be empty.")
                continue

            description = input("Enter task description (optional, press Enter to skip): ").strip()

            try:
                task_id = manager.add_task(title, description)
                print(f"Task added successfully with ID: {task_id}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            # View Task List
            print("\nCurrent Task List:")
            print(manager.display_tasks())

        elif choice == '6':
            print("Thank you for using the Console Todo App. Goodbye!")
            break
        elif choice == '3':
            # Update Task
            if not manager.get_all_tasks():
                print("No tasks available to update.")
                continue

            print("\nCurrent Task List:")
            print(manager.display_tasks())

            try:
                task_id_input = input("\nEnter the task ID to update: ").strip()
                if not task_id_input.isdigit():
                    print("Error: Task ID must be a number.")
                    continue

                task_id = int(task_id_input)

                # Check if task exists
                task = manager.find_task_by_id(task_id)
                if not task:
                    print(f"Error: Task with ID {task_id} not found.")
                    continue

                print(f"Updating task: {task.title}")

                new_title = input(f"Enter new title (current: '{task.title}', press Enter to keep current): ").strip()
                if new_title == "":
                    new_title = None  # Keep current title
                elif not new_title:  # Empty after strip but not just pressing Enter
                    print("Error: Task title cannot be empty.")
                    continue

                new_description = input(f"Enter new description (current: '{task.description}', press Enter to keep current): ").strip()
                if new_description == "":
                    new_description = None  # Keep current description

                try:
                    manager.update_task(task_id, title=new_title, description=new_description)
                    print(f"Task {task_id} updated successfully.")
                except ValueError as e:
                    print(f"Error: {e}")

            except ValueError:
                print("Error: Invalid input. Please enter a valid task ID.")

        elif choice == '4':
            # Delete Task
            if not manager.get_all_tasks():
                print("No tasks available to delete.")
                continue

            print("\nCurrent Task List:")
            print(manager.display_tasks())

            try:
                task_id_input = input("\nEnter the task ID to delete: ").strip()
                if not task_id_input.isdigit():
                    print("Error: Task ID must be a number.")
                    continue

                task_id = int(task_id_input)

                success = manager.delete_task(task_id)
                if success:
                    print(f"Task {task_id} deleted successfully.")
                else:
                    print(f"Error: Task with ID {task_id} not found.")

            except ValueError:
                print("Error: Invalid input. Please enter a valid task ID.")

        elif choice == '5':
            # Mark as Complete
            if not manager.get_all_tasks():
                print("No tasks available to mark.")
                continue

            print("\nCurrent Task List:")
            print(manager.display_tasks())

            try:
                task_id_input = input("\nEnter the task ID to toggle completion status: ").strip()
                if not task_id_input.isdigit():
                    print("Error: Task ID must be a number.")
                    continue

                task_id = int(task_id_input)

                success = manager.toggle_complete(task_id)
                if success:
                    task = manager.find_task_by_id(task_id)
                    status = "completed" if task.completed else "incomplete"
                    print(f"Task {task_id} marked as {status}.")
                else:
                    print(f"Error: Task with ID {task_id} not found.")

            except ValueError:
                print("Error: Invalid input. Please enter a valid task ID.")
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()