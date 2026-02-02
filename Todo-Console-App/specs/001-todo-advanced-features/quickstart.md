# Quickstart Guide: Todo Console App - Advanced Level Features

## Overview
This guide provides a quick introduction to implementing the advanced features for the Todo Console App: due dates and recurring tasks with console-based reminders.

## Prerequisites
- Python 3.13+ installed
- Basic understanding of Python classes and modules
- Completed implementation of Basic and Intermediate features

## Key Components to Modify

### 1. models.py - Task Model Extension
```python
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: str = "none"  # "high", "medium", "low", "none"
    tags: list[str] = None  # List of string tags
    due_datetime: Optional[datetime] = None  # Optional due date/time
    recurrence: str = "none"  # "daily", "weekly", "monthly", "none"

    def __post_init__(self):
        if self.tags is None:
            self.tags = []
```

### 2. todo_manager.py - Core Logic Extensions
Key methods to implement/extend:
- `add_task()` - Accept due_datetime and recurrence parameters
- `update_task()` - Support updating due_datetime and recurrence
- `is_overdue(task)` - Check if a task is overdue
- `process_recurrence(task_id)` - Handle recurring task generation
- `get_overdue_tasks()` - Return list of overdue tasks
- `filter_tasks()` - Extend with due date filtering
- `sort_tasks()` - Extend with due date sorting

### 3. main.py - CLI Interface Extensions
New menu options and input handling:
- Add due date input prompts during task creation
- Add recurrence selection during task creation/update
- Display due dates and recurrence indicators in task lists
- Show overdue warnings on app start and in task lists

## Implementation Steps

### Step 1: Extend Task Model
1. Add `due_datetime: Optional[datetime]` field to Task dataclass
2. Add `recurrence: str` field with default "none"
3. Update validation to handle new fields

### Step 2: Add Date Parsing Utilities
1. Create utility function to parse date strings in multiple formats
2. Handle common formats: YYYY-MM-DD, YYYY-MM-DD HH:MM, YYYY-MM-DD HH:MM:SS
3. Provide clear error messages for invalid formats

### Step 3: Implement Overdue Logic
1. Add function to check if task is overdue
2. Compare due_datetime with current time
3. Only consider incomplete tasks as potentially overdue

### Step 4: Implement Recurrence Logic
1. Add function to advance dates based on recurrence pattern
2. Handle month-end edge cases for monthly recurrence
3. Create new task instances when recurring tasks are completed

### Step 5: Update CLI Interface
1. Add prompts for due date and recurrence during task creation
2. Add display of due dates and recurrence indicators
3. Add overdue warnings to task listings

## Testing Approach
1. Test due date assignment and display
2. Test overdue detection with past dates
3. Test recurrence generation when completing tasks
4. Test month-end edge cases for monthly recurrence
5. Test integration with existing features (priorities, tags, search, etc.)

## Key Considerations
- Maintain backward compatibility with existing tasks
- Handle None values for due_datetime appropriately
- Ensure proper error handling for invalid date inputs
- Keep console output readable with new information
- Test edge cases like leap years and month-end dates