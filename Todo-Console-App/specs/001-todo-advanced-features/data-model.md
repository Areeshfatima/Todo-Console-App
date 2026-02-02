# Data Model: Todo Console App - Advanced Level Features

## Task Entity

### Fields
- `id`: int (auto-incrementing integer, primary identifier)
- `title`: str (non-empty string, required)
- `description`: str (string, optional)
- `completed`: bool (boolean indicating completion status)
- `priority`: str (string enum: "high", "medium", "low", "none")
- `tags`: list[str] (list of string tags for categorization)
- `due_datetime`: Optional[datetime] (optional datetime object representing when the task is due)
- `recurrence`: str (string enum: "daily", "weekly", "monthly", "none" indicating recurrence pattern)

### Relationships
- None (standalone entity)

### Validation Rules
- `id`: Must be unique, positive integer
- `title`: Must be non-empty string after trimming whitespace
- `completed`: Must be boolean value
- `priority`: Must be one of "high", "medium", "low", "none" (case-insensitive)
- `tags`: Must be list of non-empty strings after trimming
- `due_datetime`: If present, must be a valid datetime object
- `recurrence`: Must be one of "daily", "weekly", "monthly", "none" (case-insensitive)

### State Transitions
- `completed` can transition from False to True (mark complete) or True to False (mark incomplete)
- `due_datetime` can be set initially, updated, or cleared
- `recurrence` can be set initially, updated, or changed to "none"

## Supporting Entities

### DueDateTime
- Type: Optional[datetime]
- Represents: When the task is due (None if no due date)
- Format: Standard Python datetime object (timezone naive, local time assumption)
- Validation: If present, must represent a valid date/time

### RecurrencePattern
- Type: str (enum)
- Values: "daily", "weekly", "monthly", "none"
- Represents: Frequency at which the task repeats
- Validation: Must be one of the allowed values (case-insensitive)

### OverdueStatus
- Type: bool (computed property)
- Computed from: `due_datetime` and current system time when `completed` is False
- Logic: `due_datetime < datetime.now()` and `not completed`
- Represents: Whether a task is overdue (True) or not (False)

### DateRange
- Type: dict with "start" and "end" keys
- Format: {"start": Optional[datetime], "end": Optional[datetime]}
- Represents: Time window for filtering tasks by due date
- Validation: If both start and end are present, start must be before or equal to end

## Data Access Patterns

### Query Patterns
- Get all tasks with due dates in a specific range
- Get all overdue tasks (due_date < now and not completed)
- Get all recurring tasks (recurrence != "none")
- Filter tasks by due date and recurrence pattern
- Sort tasks by due date (ascending/descending)

### Modification Patterns
- Create task with due date and recurrence
- Update task due date
- Change task recurrence pattern
- Mark recurring task complete (triggers new instance creation)
- Clear due date or recurrence pattern

## Backward Compatibility
- Existing tasks without due_datetime or recurrence will have these fields as None/"none" respectively
- All new fields are optional or have sensible defaults
- Existing functionality remains unchanged