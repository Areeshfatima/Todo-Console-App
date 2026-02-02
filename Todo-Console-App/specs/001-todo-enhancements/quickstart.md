# Quickstart Guide: Todo Console App - Intermediate Level Features

## Overview
Quick guide to implement the intermediate-level features for the Todo Console App including priorities, tags, search, filter, and sort functionality.

## Prerequisites
- Python 3.13+ installed
- Working Basic Level Todo Console App (with models.py, todo_manager.py, main.py)
- Understanding of the existing codebase structure

## Implementation Steps

### 1. Extend the Task Model
Modify `src/models.py` to include priority and tags fields:

```python
from dataclasses import dataclass
from typing import List

@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: str = "none"  # "high", "medium", "low", "none"
    tags: List[str] = None  # List of string tags

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
        if self.priority not in ["high", "medium", "low", "none"]:
            raise ValueError(f"Invalid priority: {self.priority}")
```

### 2. Update TodoManager Class
Enhance `src/todo_manager.py` with new functionality:

#### Add methods for priority and tags handling:
- Update `add_task()` to accept priority and tags
- Update `update_task()` to handle priority and tags modification
- Add `search_tasks(keyword)` method
- Add `filter_tasks(criteria)` method
- Add `sort_tasks(sort_order)` method

### 3. Update CLI Interface
Modify `src/main.py` to include new menu options:
- Option 6: Search Tasks
- Option 7: Filter Tasks
- Option 8: Sort Tasks
- Update Add Task flow to collect priority and tags
- Update Update Task flow to modify priority and tags

### 4. Enhanced Display
Update the `display_tasks()` method to show priority indicators (H/M/L/N) and tags ([tag1, tag2]).

## Key Implementation Points

### Input Normalization
- Accept priority inputs: 'h', 'high', 'm', 'medium', 'l', 'low' (case-insensitive)
- Convert to standardized format: "high", "medium", "low", "none"
- Handle comma-separated tags and split into list

### Validation
- Validate priority values during creation/update
- Ensure tags are non-empty after trimming
- Automatically deduplicate tags while preserving order

### Search Implementation
- Case-insensitive search across title, description, and tags
- Return list of matching tasks
- Handle empty results gracefully

### Filter Implementation
- Support filtering by completion status, priority, and tags
- Allow combination of multiple filter criteria
- Return appropriate message when no matches found

### Sort Implementation
- Support sorting by priority (high → medium → low → none)
- Support alphabetical sorting by title
- Apply to currently filtered/searched results

## Testing Checklist
- [ ] Add task with priority and tags
- [ ] Update task priority and tags
- [ ] View tasks with priority and tags displayed correctly
- [ ] Search tasks by keyword in title/description/tags
- [ ] Filter tasks by status/priority
- [ ] Sort tasks by priority/title
- [ ] Verify backward compatibility with existing tasks
- [ ] Test error handling for invalid inputs