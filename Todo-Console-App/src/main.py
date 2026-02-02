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

    # Check for overdue tasks and display a reminder if any exist
    overdue_count = manager.count_overdue_tasks()
    if overdue_count > 0:
        print(f"REMINDER: You have {overdue_count} overdue task{'s' if overdue_count != 1 else ''}!")
        print("Use 'View Task List' to see overdue tasks marked with [OVERDUE!]")

    print("Application is ready. Use the CLI interface to manage your tasks.")

    while True:
        print("\nConsole Todo App Menu:")
        print("1. Add Task")
        print("2. View Task List")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark as Complete")
        print("6. Search Tasks")
        print("7. Filter Tasks")
        print("8. Sort Tasks")
        print("9. Filter by Due Date Range")
        print("10. Sort by Due Date")
        print("11. Exit")

        choice = input("\nEnter your choice (1-11): ").strip()

        if choice == '1':
            # Add Task
            title = input("Enter task title: ").strip()

            if not title:
                print("Error: Task title cannot be empty.")
                continue

            description = input("Enter task description (optional, press Enter to skip): ").strip()

            # Get priority input
            priority_input = input("Enter priority (h/high, m/medium, l/low, n/none - default: none): ").strip()
            if not priority_input:
                priority_input = "none"

            # Get tags input
            tags_input = input("Enter tags (comma-separated, optional, press Enter to skip): ").strip()
            tags_list = manager.normalize_tags(tags_input) if tags_input else []

            # Get due date input
            due_date_input = input("Enter due date (optional, format: YYYY-MM-DD or YYYY-MM-DD HH:MM, press Enter to skip): ").strip()

            # Get recurrence input
            recurrence_input = input("Enter recurrence (optional, daily/weekly/monthly/none - default: none): ").strip()
            if not recurrence_input:
                recurrence_input = "none"

            try:
                task_id = manager.add_task(title, description, priority_input, tags_list, due_date_input, recurrence_input)
                print(f"Task added successfully with ID: {task_id}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            # View Task List
            print("\nCurrent Task List:")
            print(manager.display_tasks())

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

                # Get new priority
                priority_input = input(f"Enter new priority (current: {task.priority}, h/high, m/medium, l/low, n/none, press Enter to keep current): ").strip()
                if priority_input == "":
                    priority_input = None  # Keep current priority
                elif not priority_input:
                    priority_input = None  # Keep current priority

                # Get new tags
                tags_input = input(f"Enter new tags (current: {', '.join(task.tags) if task.tags else 'none'}, comma-separated, press Enter to keep current): ").strip()
                if tags_input == "":
                    tags_list = None  # Keep current tags
                else:
                    tags_list = manager.normalize_tags(tags_input) if tags_input else []

                # Get new due date
                current_due_date = ""
                if task.due_datetime:
                    from utils import format_datetime
                    current_due_date = format_datetime(task.due_datetime)

                due_date_input = input(f"Enter new due date (current: {current_due_date}, format: YYYY-MM-DD or YYYY-MM-DD HH:MM, press Enter to keep current, or leave blank to clear): ").strip()
                if due_date_input == "":
                    due_date_input = None  # Keep current due date

                # Get new recurrence
                recurrence_input = input(f"Enter new recurrence (current: {task.recurrence}, daily/weekly/monthly/none, press Enter to keep current): ").strip()
                if recurrence_input == "":
                    recurrence_input = None  # Keep current recurrence

                try:
                    manager.update_task(task_id, title=new_title, description=new_description, priority=priority_input, tags=tags_list, due_datetime_str=due_date_input, recurrence=recurrence_input)
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

        elif choice == '6':
            # Search Tasks
            if not manager.get_all_tasks():
                print("No tasks available to search.")
                continue

            keyword = input("Enter keyword to search for: ").strip()
            if not keyword:
                print("Error: Search keyword cannot be empty.")
                continue

            search_results = manager.search_tasks(keyword)
            if search_results:
                print(f"\nSearch Results for '{keyword}':")
                # Temporarily set manager's task list to search results for display
                original_tasks = manager.task_list
                manager.task_list = search_results
                print(manager.display_tasks())
                # Restore original task list
                manager.task_list = original_tasks
            else:
                print(f"No tasks found matching '{keyword}'.")

        elif choice == '7':
            # Filter Tasks
            if not manager.get_all_tasks():
                print("No tasks available to filter.")
                continue

            print("\nFilter Options:")
            print("1. By Completion Status")
            print("2. By Priority")
            print("3. By Tags")
            print("4. Combined Filters")

            filter_choice = input("Enter filter choice (1-4): ").strip()

            status_filter = None
            priority_filter = None
            tags_filter = None

            if filter_choice == '1':
                status_choice = input("Enter status to filter (complete/incomplete/all): ").strip().lower()
                if status_choice in ['complete', 'incomplete', 'all']:
                    status_filter = status_choice
                else:
                    print("Invalid status. Please enter 'complete', 'incomplete', or 'all'.")
                    continue

            elif filter_choice == '2':
                priority_input = input("Enter priority to filter (h/high, m/medium, l/low, n/none): ").strip().lower()
                if priority_input:
                    priority_filter = priority_input
                else:
                    print("Invalid priority input.")
                    continue

            elif filter_choice == '3':
                tags_input = input("Enter tags to filter (comma-separated): ").strip()
                if tags_input:
                    tags_filter = manager.normalize_tags(tags_input)
                else:
                    print("No tags provided for filtering.")
                    continue

            elif filter_choice == '4':
                status_choice = input("Enter status to filter (complete/incomplete/all, press Enter to skip): ").strip().lower()
                if status_choice in ['complete', 'incomplete', 'all']:
                    status_filter = status_choice
                elif status_choice == '':
                    status_filter = None
                else:
                    print("Invalid status. Please enter 'complete', 'incomplete', or 'all'.")
                    continue

                priority_input = input("Enter priority to filter (h/high, m/medium, l/low, n/none, press Enter to skip): ").strip().lower()
                if priority_input:
                    priority_filter = priority_input
                elif priority_input == '':
                    priority_filter = None
                else:
                    print("Invalid priority input.")
                    continue

                tags_input = input("Enter tags to filter (comma-separated, press Enter to skip): ").strip()
                if tags_input:
                    tags_filter = manager.normalize_tags(tags_input)
                elif tags_input == '':
                    tags_filter = None
                else:
                    print("Invalid tags input.")
                    continue
            else:
                print("Invalid filter choice.")
                continue

            # Apply filters
            filtered_tasks = manager.filter_tasks(status=status_filter, priority=priority_filter, tags=tags_filter)

            if filtered_tasks:
                print("\nFiltered Results:")
                # Temporarily set manager's task list to filtered results for display
                original_tasks = manager.task_list
                manager.task_list = filtered_tasks
                print(manager.display_tasks())
                # Restore original task list
                manager.task_list = original_tasks
            else:
                print("No tasks match the filter criteria.")

        elif choice == '8':
            # Sort Tasks
            if not manager.get_all_tasks():
                print("No tasks available to sort.")
                continue

            print("\nSort Options:")
            print("1. By Priority (high to low)")
            print("2. By Title (A to Z)")
            print("3. By ID (ascending)")

            sort_choice = input("Enter sort choice (1-3): ").strip()

            if sort_choice == '1':
                sorted_tasks = manager.sort_tasks(manager.get_all_tasks(), "priority", "asc")
            elif sort_choice == '2':
                sorted_tasks = manager.sort_tasks(manager.get_all_tasks(), "title", "asc")
            elif sort_choice == '3':
                sorted_tasks = manager.sort_tasks(manager.get_all_tasks(), "id", "asc")
            else:
                print("Invalid sort choice.")
                continue

            print("\nSorted Results:")
            # Temporarily set manager's task list to sorted results for display
            original_tasks = manager.task_list
            manager.task_list = sorted_tasks
            print(manager.display_tasks())
            # Restore original task list
            manager.task_list = original_tasks

        elif choice == '9':
            # Filter by Due Date Range
            if not manager.get_all_tasks():
                print("No tasks available to filter.")
                continue

            print("\nFilter by Due Date Range:")

            start_date_input = input("Enter start date (optional, format: YYYY-MM-DD or YYYY-MM-DD HH:MM, press Enter to skip): ").strip()
            end_date_input = input("Enter end date (optional, format: YYYY-MM-DD or YYYY-MM-DD HH:MM, press Enter to skip): ").strip()

            from utils import parse_date_string
            start_date = parse_date_string(start_date_input) if start_date_input else None
            end_date = parse_date_string(end_date_input) if end_date_input else None

            # Create due date range filter
            due_date_range = {}
            if start_date:
                due_date_range["start"] = start_date
            if end_date:
                due_date_range["end"] = end_date

            filtered_tasks = manager.filter_tasks(due_date_range=due_date_range)

            if filtered_tasks:
                print("\nFiltered Results:")
                # Temporarily set manager's task list to filtered results for display
                original_tasks = manager.task_list
                manager.task_list = filtered_tasks
                print(manager.display_tasks())
                # Restore original task list
                manager.task_list = original_tasks
            else:
                print("No tasks match the date range criteria.")

        elif choice == '10':
            # Sort by Due Date
            if not manager.get_all_tasks():
                print("No tasks available to sort.")
                continue

            print("\nSort by Due Date Options:")
            print("1. Earliest to Latest")
            print("2. Latest to Earliest")

            sort_choice = input("Enter sort choice (1-2): ").strip()

            if sort_choice == '1':
                sorted_tasks = manager.sort_tasks(manager.get_all_tasks(), "due_date", "asc")
            elif sort_choice == '2':
                sorted_tasks = manager.sort_tasks(manager.get_all_tasks(), "due_date", "desc")
            else:
                print("Invalid sort choice.")
                continue

            print("\nSorted Results:")
            # Temporarily set manager's task list to sorted results for display
            original_tasks = manager.task_list
            manager.task_list = sorted_tasks
            print(manager.display_tasks())
            # Restore original task list
            manager.task_list = original_tasks

        elif choice == '11':
            print("Thank you for using the Console Todo App. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 11.")


if __name__ == "__main__":
    main()