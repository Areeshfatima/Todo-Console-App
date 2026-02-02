# API Contracts: Task Operations

## Core Operations

### Add Task
- **Method**: add_task(title: str, description: str = "") -> int
- **Parameters**:
  - `title` (str): Non-empty string for task title
  - `description` (str, optional): Description string, defaults to empty string
- **Returns**: int - The auto-generated ID of the new task
- **Errors**: ValueError if title is empty after stripping whitespace
- **Post-condition**: New Task object added to in-memory list with completed=False

### Get Task
- **Method**: get_task(task_id: int) -> Optional[Task]
- **Parameters**:
  - `task_id` (int): Unique identifier of the task to retrieve
- **Returns**: Task object if found, None if not found
- **Errors**: None - returns None for invalid IDs

### Get All Tasks
- **Method**: get_all_tasks() -> List[Task]
- **Parameters**: None
- **Returns**: List of all Task objects in the system, empty list if none exist
- **Errors**: None

### Update Task
- **Method**: update_task(task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool
- **Parameters**:
  - `task_id` (int): Unique identifier of the task to update
  - `title` (Optional[str]): New title if provided
  - `description` (Optional[str]): New description if provided
- **Returns**: bool - True if update successful, False if task not found
- **Errors**: ValueError if title is provided but is empty after stripping whitespace
- **Post-condition**: Task properties updated only if values provided

### Delete Task
- **Method**: delete_task(task_id: int) -> bool
- **Parameters**:
  - `task_id` (int): Unique identifier of the task to delete
- **Returns**: bool - True if deletion successful, False if task not found
- **Post-condition**: Task removed from in-memory list, ID remains unavailable

### Toggle Complete
- **Method**: toggle_complete(task_id: int) -> bool
- **Parameters**:
  - `task_id` (int): Unique identifier of the task to toggle
- **Returns**: bool - True if toggle successful, False if task not found
- **Post-condition**: Task.completed property switched from True to False or False to True

## Data Model Contract

### Task Class
- **Properties**:
  - `id` (int): Unique positive integer identifier
  - `title` (str): Non-empty string after whitespace trimming
  - `description` (str): Any string, including empty
  - `completed` (bool): Boolean indicating completion status