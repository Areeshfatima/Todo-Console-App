"""
Todo Manager for the Console Todo App.

This module contains the TodoManager class that handles all operations and in-memory storage.
"""

from datetime import datetime
from typing import List, Optional
from models import Task
from utils import parse_date_string, format_datetime, advance_date_by_recurrence, is_overdue


class TodoManager:
    """
    Manages the collection of tasks in memory.

    Handles all operations related to tasks including adding, viewing, updating, deleting,
    and toggling completion status.
    """

    def __init__(self):
        """Initialize the TodoManager with an empty task list and starting ID counter."""
        self.task_list: List[Task] = []
        self.next_id: int = 1

    def get_next_available_id(self) -> int:
        """
        Get the next available ID for a new task.

        Returns:
            int: The next available ID
        """
        return self.next_id

    def validate_title(self, title: str) -> bool:
        """
        Validate that a title is not empty after stripping whitespace.

        Args:
            title (str): The title to validate

        Returns:
            bool: True if the title is valid, False otherwise
        """
        return bool(title.strip())

    def validate_priority(self, priority: str) -> bool:
        """
        Validate that a priority is one of the allowed values.

        Args:
            priority (str): The priority to validate

        Returns:
            bool: True if the priority is valid, False otherwise
        """
        valid_priorities = ["high", "medium", "low", "none"]
        return priority.lower() in valid_priorities

    def normalize_priority(self, priority: str) -> str:
        """
        Normalize priority input to standard format.

        Args:
            priority (str): The priority input to normalize

        Returns:
            str: The normalized priority value
        """
        priority_map = {
            'h': 'high',
            'high': 'high',
            'm': 'medium',
            'medium': 'medium',
            'l': 'low',
            'low': 'low',
            'n': 'none',
            'none': 'none'
        }

        normalized_priority = priority.lower().strip()
        if normalized_priority in priority_map:
            return priority_map[normalized_priority]
        return normalized_priority  # Return as-is if not in map, validation will catch it

    def normalize_tags(self, tags_str: str) -> List[str]:
        """
        Normalize comma-separated tags string to a list of trimmed, non-empty tags.

        Args:
            tags_str (str): Comma-separated tags string

        Returns:
            List[str]: List of normalized tags
        """
        if not tags_str:
            return []

        tags = [tag.strip() for tag in tags_str.split(',')]
        # Filter out empty tags and return unique tags while preserving order
        seen = set()
        normalized_tags = []
        for tag in tags:
            if tag and tag not in seen:
                normalized_tags.append(tag)
                seen.add(tag)
        return normalized_tags

    def add_task(self, title: str, description: str = "", priority: str = "none", tags: List[str] = None, due_datetime_str: str = "", recurrence: str = "none") -> int:
        """
        Add a new task to the task list.

        Args:
            title (str): The title of the task (required, non-empty)
            description (str): The description of the task (optional)
            priority (str): The priority level of the task (default: "none")
            tags (List[str]): List of tags for the task (optional)
            due_datetime_str (str): String representation of the due date/time (optional)
            recurrence (str): Recurrence pattern of the task (default: "none")

        Returns:
            int: The ID of the newly created task

        Raises:
            ValueError: If the title is empty after stripping whitespace, priority is invalid,
                       due_datetime_str is in invalid format, or recurrence is invalid
        """
        if not self.validate_title(title):
            raise ValueError("Task title cannot be empty or contain only whitespace")

        # Normalize and validate priority
        normalized_priority = self.normalize_priority(priority)
        if not self.validate_priority(normalized_priority):
            raise ValueError(f"Invalid priority: {priority}. Must be one of: high, medium, low, none")

        # Parse due date if provided
        due_datetime = None
        if due_datetime_str:
            due_datetime = parse_date_string(due_datetime_str)
            if due_datetime is None:
                raise ValueError(f"Invalid date format: {due_datetime_str}. Use YYYY-MM-DD or YYYY-MM-DD HH:MM format.")

        # Validate recurrence
        valid_recurrences = ["daily", "weekly", "monthly", "none"]
        if recurrence.lower() not in valid_recurrences:
            raise ValueError(f"Invalid recurrence: {recurrence}. Must be one of: {valid_recurrences}")

        # Create a new task with the next available ID
        task_id = self.get_next_available_id()
        new_task = Task(
            id=task_id,
            title=title,
            description=description,
            completed=False,
            priority=normalized_priority,
            tags=tags if tags is not None else [],
            due_datetime=due_datetime,
            recurrence=recurrence.lower()
        )

        # Add the task to the list
        self.task_list.append(new_task)

        # Increment the next_id for the next task
        self.next_id += 1

        return task_id

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the task list.

        Returns:
            List[Task]: A list of all Task objects in the system
        """
        return self.task_list.copy()

    def display_tasks(self) -> str:
        """
        Create a formatted display of all tasks.

        Returns:
            str: Formatted string representation of all tasks with ID, status indicator,
                 priority indicator, tags, due date, recurrence, title, and description
        """
        if not self.task_list:
            return "No tasks in the list."

        output_lines = []

        for task in self.task_list:
            status_indicator = "[✓]" if task.completed else "[ ]"

            # Create priority indicator
            priority_map = {
                "high": "H",
                "medium": "M",
                "low": "L",
                "none": "N"
            }
            priority_indicator = f"[{priority_map.get(task.priority, 'N')}]"

            # Format tags
            tags_str = f" [{', '.join(task.tags)}]" if task.tags else ""

            # Format due date
            due_date_str = ""
            if task.due_datetime:
                formatted_date = format_datetime(task.due_datetime)
                due_date_str = f" ({formatted_date})"

                # Add overdue indicator if task is overdue
                if is_overdue(task.due_datetime) and not task.completed:
                    due_date_str += " [OVERDUE!]"

            # Format recurrence indicator
            recurrence_str = ""
            if task.recurrence and task.recurrence != "none":
                recurrence_str = f" [RECURSING-{task.recurrence.upper()}]"

            line = f"{task.id}. {status_indicator} {priority_indicator}{tags_str}{due_date_str}{recurrence_str} {task.title}"

            if task.description:
                line += f"\n   Description: {task.description}"

            output_lines.append(line)

        return "\n".join(output_lines)

    def toggle_complete(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task by ID.
        If the task is recurring and being marked as complete, create a new instance with the due date advanced by the recurrence interval.

        Args:
            task_id (int): The ID of the task to toggle

        Returns:
            bool: True if the toggle was successful, False if task was not found
        """
        for task in self.task_list:
            if task.id == task_id:
                # Check if we're marking a recurring task as complete
                was_completed = task.completed
                task.completed = not task.completed

                # If we're marking the task as complete and it's recurring, create a new instance
                if not was_completed and task.completed and task.recurrence and task.recurrence != "none":
                    # Create a new instance of the recurring task
                    new_due_datetime = None
                    if task.due_datetime:
                        new_due_datetime = advance_date_by_recurrence(task.due_datetime, task.recurrence)

                    # Create a new task with the next available ID
                    new_task_id = self.get_next_available_id()
                    new_task = Task(
                        id=new_task_id,
                        title=task.title,
                        description=task.description,
                        completed=False,  # New recurring task starts as incomplete
                        priority=task.priority,
                        tags=task.tags.copy(),  # Copy the tags
                        due_datetime=new_due_datetime,
                        recurrence=task.recurrence  # Keep the same recurrence pattern
                    )

                    # Add the new task to the list
                    self.task_list.append(new_task)

                    # Increment the next_id for the next task
                    self.next_id += 1

                return True
        return False

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None, completed: Optional[bool] = None, priority: Optional[str] = None, tags: Optional[List[str]] = None, due_datetime_str: Optional[str] = None, recurrence: Optional[str] = None) -> bool:
        """
        Update an existing task by ID.

        Args:
            task_id (int): The ID of the task to update
            title (Optional[str]): New title for the task (optional)
            description (Optional[str]): New description for the task (optional)
            completed (Optional[bool]): New completion status for the task (optional)
            priority (Optional[str]): New priority for the task (optional)
            tags (Optional[List[str]]): New tags for the task (optional)
            due_datetime_str (Optional[str]): New due date/time string for the task (optional)
            recurrence (Optional[str]): New recurrence pattern for the task (optional)

        Returns:
            bool: True if the update was successful, False if task was not found
        """
        for task in self.task_list:
            if task.id == task_id:
                # Update title if provided
                if title is not None:
                    if not self.validate_title(title):
                        raise ValueError("Task title cannot be empty or contain only whitespace")
                    task.title = title.strip()

                # Update description if provided
                if description is not None:
                    task.description = description

                # Update completion status if provided
                if completed is not None:
                    task.completed = completed

                # Update priority if provided
                if priority is not None:
                    normalized_priority = self.normalize_priority(priority)
                    if not self.validate_priority(normalized_priority):
                        raise ValueError(f"Invalid priority: {priority}. Must be one of: high, medium, low, none")
                    task.priority = normalized_priority

                # Update tags if provided
                if tags is not None:
                    task.tags = tags

                # Update due datetime if provided
                if due_datetime_str is not None:
                    if due_datetime_str == "":
                        # If empty string, set to None (clear the due date)
                        task.due_datetime = None
                    else:
                        parsed_datetime = parse_date_string(due_datetime_str)
                        if parsed_datetime is None:
                            raise ValueError(f"Invalid date format: {due_datetime_str}. Use YYYY-MM-DD or YYYY-MM-DD HH:MM format.")
                        task.due_datetime = parsed_datetime

                # Update recurrence if provided
                if recurrence is not None:
                    valid_recurrences = ["daily", "weekly", "monthly", "none"]
                    if recurrence.lower() not in valid_recurrences:
                        raise ValueError(f"Invalid recurrence: {recurrence}. Must be one of: {valid_recurrences}")
                    task.recurrence = recurrence.lower()

                return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the deletion was successful, False if task was not found
        """
        for i, task in enumerate(self.task_list):
            if task.id == task_id:
                del self.task_list[i]
                return True
        return False

    def find_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Find a task by its ID.

        Args:
            task_id (int): The ID of the task to find

        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        for task in self.task_list:
            if task.id == task_id:
                return task
        return None

    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Search tasks by keyword across title, description, and tags.

        Args:
            keyword (str): The keyword to search for (case-insensitive)

        Returns:
            List[Task]: List of tasks that match the search criteria
        """
        keyword_lower = keyword.lower().strip()
        if not keyword_lower:
            return []

        matching_tasks = []
        for task in self.task_list:
            # Check if keyword is in title, description, or tags
            if (keyword_lower in task.title.lower() or
                keyword_lower in task.description.lower() or
                any(keyword_lower in tag.lower() for tag in task.tags)):
                matching_tasks.append(task)

        return matching_tasks

    def filter_tasks(self, status: Optional[str] = None, priority: Optional[str] = None, tags: Optional[List[str]] = None) -> List[Task]:
        """
        Filter tasks by status, priority, or tags.

        Args:
            status (Optional[str]): Filter by completion status ("complete", "incomplete", "all")
            priority (Optional[str]): Filter by priority level ("high", "medium", "low", "none")
            tags (Optional[List[str]]): Filter by presence of specific tags

        Returns:
            List[Task]: List of tasks that match the filter criteria
        """
        filtered_tasks = []

        for task in self.task_list:
            # Apply status filter
            if status is not None and status.lower() != "all":
                if status.lower() == "complete" and not task.completed:
                    continue
                elif status.lower() == "incomplete" and task.completed:
                    continue

            # Apply priority filter
            if priority is not None:
                normalized_priority = self.normalize_priority(priority)
                if task.priority != normalized_priority:
                    continue

            # Apply tags filter
            if tags is not None and tags:
                # Check if task has all the specified tags
                task_tags_set = set(task.tags)
                required_tags_set = set(tags)
                if not required_tags_set.issubset(task_tags_set):
                    continue

            filtered_tasks.append(task)

        return filtered_tasks

    def sort_tasks(self, tasks: List[Task], field: str, direction: str = "asc") -> List[Task]:
        """
        Sort tasks by specified field and direction.

        Args:
            tasks (List[Task]): List of tasks to sort
            field (str): Field to sort by ("priority", "title", "id", "due_date")
            direction (str): Sort direction ("asc" or "desc")

        Returns:
            List[Task]: New list of tasks in sorted order
        """
        # Define priority order for sorting
        priority_order = {"high": 0, "medium": 1, "low": 2, "none": 3}

        if field.lower() == "priority":
            sorted_tasks = sorted(
                tasks,
                key=lambda t: priority_order.get(t.priority, 4),
                reverse=(direction.lower() == "desc")
            )
        elif field.lower() == "title":
            sorted_tasks = sorted(
                tasks,
                key=lambda t: t.title.lower(),
                reverse=(direction.lower() == "desc")
            )
        elif field.lower() == "id":
            sorted_tasks = sorted(
                tasks,
                key=lambda t: t.id,
                reverse=(direction.lower() == "desc")
            )
        elif field.lower() == "due_date":
            # Sort by due date, with None values at the end
            sorted_tasks = sorted(
                tasks,
                key=lambda t: (t.due_datetime is None, t.due_datetime),
                reverse=(direction.lower() == "desc")
            )
        else:
            # Default to ID if field is invalid
            sorted_tasks = sorted(
                tasks,
                key=lambda t: t.id,
                reverse=(direction.lower() == "desc")
            )

        return sorted_tasks

    def get_overdue_tasks(self) -> List[Task]:
        """
        Get all tasks that are overdue (have a due date in the past and are not completed).

        Returns:
            List[Task]: List of overdue tasks
        """
        overdue_tasks = []
        for task in self.task_list:
            if is_overdue(task.due_datetime) and not task.completed:
                overdue_tasks.append(task)
        return overdue_tasks

    def count_overdue_tasks(self) -> int:
        """
        Count the number of overdue tasks.

        Returns:
            int: Number of overdue tasks
        """
        return len(self.get_overdue_tasks())

    def filter_tasks(self, status: Optional[str] = None, priority: Optional[str] = None, tags: Optional[List[str]] = None, due_date_range: Optional[dict] = None, overdue_only: bool = False) -> List[Task]:
        """
        Filter tasks by status, priority, tags, due date range, or overdue status.

        Args:
            status (Optional[str]): Filter by completion status ("complete", "incomplete", "all")
            priority (Optional[str]): Filter by priority level ("high", "medium", "low", "none")
            tags (Optional[List[str]]): Filter by presence of specific tags
            due_date_range (Optional[dict]): Filter by due date range with "start" and "end" datetime objects
            overdue_only (bool): Filter to show only overdue tasks

        Returns:
            List[Task]: List of tasks that match the filter criteria
        """
        filtered_tasks = []

        for task in self.task_list:
            # Apply status filter
            if status is not None and status.lower() != "all":
                if status.lower() == "complete" and not task.completed:
                    continue
                elif status.lower() == "incomplete" and task.completed:
                    continue

            # Apply priority filter
            if priority is not None:
                normalized_priority = self.normalize_priority(priority)
                if task.priority != normalized_priority:
                    continue

            # Apply tags filter
            if tags is not None and tags:
                # Check if task has all the specified tags
                task_tags_set = set(task.tags)
                required_tags_set = set(tags)
                if not required_tags_set.issubset(task_tags_set):
                    continue

            # Apply due date range filter
            if due_date_range is not None:
                if task.due_datetime is None:
                    continue
                if due_date_range.get("start") and task.due_datetime < due_date_range["start"]:
                    continue
                if due_date_range.get("end") and task.due_datetime > due_date_range["end"]:
                    continue

            # Apply overdue only filter
            if overdue_only and (not is_overdue(task.due_datetime) or task.completed):
                continue

            filtered_tasks.append(task)

        return filtered_tasks