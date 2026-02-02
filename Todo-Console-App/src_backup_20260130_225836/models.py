"""
Models for the Console Todo App.

This module contains the Task dataclass that represents a single todo item.
"""

from dataclasses import dataclass


@dataclass
class Task:
    """
    Represents a single todo item in the application.

    Attributes:
        id (int): Unique auto-incrementing identifier for the task
        title (str): Non-empty string representing the task title
        description (str): String representing the task description (optional, can be empty)
        completed (bool): Boolean indicating whether the task is completed (True) or incomplete (False)
    """

    id: int
    title: str
    description: str = ""
    completed: bool = False

    def __post_init__(self):
        """Validate that the title is non-empty after initialization."""
        if not self.title.strip():
            raise ValueError("Task title cannot be empty or contain only whitespace")

        # Update the title to be stripped of leading/trailing whitespace
        self.title = self.title.strip()