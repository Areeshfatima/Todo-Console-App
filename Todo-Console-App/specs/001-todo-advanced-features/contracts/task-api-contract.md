# API Contract: Task Management with Due Dates and Recurrence

## Overview
This contract defines the interfaces and behaviors for the enhanced task management system with due dates and recurrence functionality.

## Task Model Contract

### Task Class Definition
```python
@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: str = "none"  # Literal["high", "medium", "low", "none"]
    tags: list[str] = None
    due_datetime: Optional[datetime] = None
    recurrence: str = "none"  # Literal["daily", "weekly", "monthly", "none"]
```

### Field Requirements
- `due_datetime`: Optional datetime object, defaults to None
- `recurrence`: String enum, one of ["daily", "weekly", "monthly", "none"], defaults to "none"

## Method Contracts

### TodoManager.add_task
**Signature**: `add_task(title: str, description: str = "", priority: str = "none", tags: list[str] = [], due_datetime_str: Optional[str] = None, recurrence: str = "none") -> int`

**Preconditions**:
- title must be non-empty string
- priority must be one of ["high", "medium", "low", "none"] (case-insensitive)
- tags must be list of non-empty strings
- due_datetime_str must be in valid format (YYYY-MM-DD or YYYY-MM-DD HH:MM) or None
- recurrence must be one of ["daily", "weekly", "monthly", "none"] (case-insensitive)

**Postconditions**:
- Creates new Task instance with provided parameters
- Sets due_datetime from parsed due_datetime_str or None
- Sets recurrence to validated value
- Assigns unique ID
- Returns the assigned ID

**Exceptions**:
- `ValueError` if any parameter validation fails

### TodoManager.update_task
**Signature**: `update_task(task_id: int, title: Optional[str] = None, description: Optional[str] = None, priority: Optional[str] = None, tags: Optional[list[str]] = None, due_datetime_str: Optional[str] = None, recurrence: Optional[str] = None) -> bool`

**Preconditions**:
- task_id must exist in task list
- If provided, due_datetime_str must be in valid format or None
- If provided, recurrence must be valid value or None

**Postconditions**:
- Updates specified fields of existing task
- Returns True if task was found and updated, False otherwise

**Exceptions**:
- `ValueError` if any parameter validation fails

### TodoManager.is_overdue
**Signature**: `is_overdue(task: Task) -> bool`

**Preconditions**:
- task must be a valid Task instance

**Postconditions**:
- Returns True if task.due_datetime is not None and less than current time and task.completed is False
- Returns False otherwise

### TodoManager.process_recurrence
**Signature**: `process_recurrence(task_id: int) -> Optional[int]`

**Preconditions**:
- task_id must exist in task list
- task must have recurrence != "none"

**Postconditions**:
- Creates new task instance with same properties as original
- Advances due date based on recurrence pattern
- Returns ID of new task instance or None if creation fails

**Exceptions**:
- `ValueError` if task_id doesn't exist or task is not recurring

### TodoManager.get_overdue_tasks
**Signature**: `get_overdue_tasks() -> list[Task]`

**Postconditions**:
- Returns list of all tasks that are overdue (per is_overdue logic)

### TodoManager.filter_tasks (Extended)
**Signature**: `filter_tasks(status: Optional[str] = None, priority: Optional[str] = None, tags: Optional[list[str]] = None, due_date_range: Optional[dict] = None, overdue_only: bool = False) -> list[Task]`

**Preconditions**:
- If due_date_range provided, must have "start" and/or "end" keys with datetime values
- overdue_only must be boolean

**Postconditions**:
- Returns filtered list of tasks based on all provided criteria
- If overdue_only=True, only returns tasks that are overdue

### TodoManager.sort_tasks (Extended)
**Signature**: `sort_tasks(tasks: list[Task], sort_by: str = "id", order: str = "asc") -> list[Task]`

**Preconditions**:
- sort_by must be one of ["id", "title", "priority", "due_date"]
- order must be "asc" or "desc"

**Postconditions**:
- Returns sorted list of tasks
- If sort_by is "due_date", sorts by due_datetime (None values at end)

## CLI Interface Contract

### Input Validation
All date inputs must accept:
- YYYY-MM-DD format (e.g., "2026-02-01")
- YYYY-MM-DD HH:MM format (e.g., "2026-02-01 14:00")
- YYYY-MM-DD HH:MM:SS format (e.g., "2026-02-01 14:00:30")

### Display Format
All due dates in output must be displayed in "YYYY-MM-DD HH:MM" format.

### Error Messages
- Invalid date format: "Error: Invalid date format. Please use YYYY-MM-DD or YYYY-MM-DD HH:MM format."
- Invalid recurrence: "Error: Invalid recurrence. Please use 'daily', 'weekly', 'monthly', or 'none'."
- Overdue indicator: "[OVERDUE]" prefix for overdue tasks
- Recurrence indicator: "[RECURRING-DAILY/WEEKLY/MONTHLY]" suffix for recurring tasks