"""
Todo Manager for the Console Todo App.

This module contains the TodoManager class that handles all operations and in-memory storage.
"""

from typing import List, Optional
from models import Task


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

    def add_task(self, title: str, description: str = "") -> int:
        """
        Add a new task to the task list.

        Args:
            title (str): The title of the task (required, non-empty)
            description (str): The description of the task (optional)

        Returns:
            int: The ID of the newly created task

        Raises:
            ValueError: If the title is empty after stripping whitespace
        """
        if not self.validate_title(title):
            raise ValueError("Task title cannot be empty or contain only whitespace")

        # Create a new task with the next available ID
        task_id = self.get_next_available_id()
        new_task = Task(id=task_id, title=title, description=description, completed=False)

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
                 title, and description
        """
        if not self.task_list:
            return "No tasks in the list."

        output_lines = []

        for task in self.task_list:
            status_indicator = "[✓]" if task.completed else "[ ]"
            line = f"{task.id}. {status_indicator} {task.title}"

            if task.description:
                line += f"\n   Description: {task.description}"

            output_lines.append(line)

        return "\n".join(output_lines)

    def toggle_complete(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task by ID.

        Args:
            task_id (int): The ID of the task to toggle

        Returns:
            bool: True if the toggle was successful, False if task was not found
        """
        for task in self.task_list:
            if task.id == task_id:
                task.completed = not task.completed
                return True
        return False

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None, completed: Optional[bool] = None) -> bool:
        """
        Update an existing task by ID.

        Args:
            task_id (int): The ID of the task to update
            title (Optional[str]): New title for the task (optional)
            description (Optional[str]): New description for the task (optional)
            completed (Optional[bool]): New completion status for the task (optional)

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