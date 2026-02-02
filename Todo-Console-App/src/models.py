"""
Models for the Console Todo App.

This module contains the Task dataclass that represents a single todo item.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class Task:
    """
    Represents a single todo item in the application.

    Attributes:
        id (int): Unique auto-incrementing identifier for the task
        title (str): Non-empty string representing the task title
        description (str): String representing the task description (optional, can be empty)
        completed (bool): Boolean indicating whether the task is completed (True) or incomplete (False)
        priority (str): Priority level of the task ("high", "medium", "low", or "none")
        tags (List[str]): List of string tags for categorizing the task
        due_datetime (Optional[datetime]): Optional datetime object representing when the task is due
        recurrence (str): Recurrence pattern of the task ("daily", "weekly", "monthly", or "none")
    """

    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: str = "none"  # "high", "medium", "low", "none"
    tags: List[str] = None  # List of string tags
    due_datetime: Optional[datetime] = None  # Optional due date/time
    recurrence: str = "none"  # "daily", "weekly", "monthly", "none"

    def __post_init__(self):
        """Validate that the title is non-empty after initialization."""
        if not self.title.strip():
            raise ValueError("Task title cannot be empty or contain only whitespace")

        # Update the title to be stripped of leading/trailing whitespace
        self.title = self.title.strip()

        # Initialize tags as empty list if None
        if self.tags is None:
            self.tags = []

        # Validate and normalize priority
        valid_priorities = ["high", "medium", "low", "none"]
        if self.priority not in valid_priorities:
            raise ValueError(f"Invalid priority: {self.priority}. Must be one of {valid_priorities}")

        # Normalize priority to lowercase
        self.priority = self.priority.lower()

        # Validate and normalize recurrence
        valid_recurrences = ["daily", "weekly", "monthly", "none"]
        if self.recurrence not in valid_recurrences:
            raise ValueError(f"Invalid recurrence: {self.recurrence}. Must be one of {valid_recurrences}")

        # Normalize recurrence to lowercase
        self.recurrence = self.recurrence.lower()