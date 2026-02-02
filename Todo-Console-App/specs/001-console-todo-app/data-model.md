# Data Model: Console Todo App

## Entity: Task

**Description**: Represents a single todo item in the application

**Fields**:
- `id` (int): Unique auto-incrementing identifier for the task
- `title` (str): Non-empty string representing the task title
- `description` (str): String representing the task description (optional, can be empty)
- `completed` (bool): Boolean indicating whether the task is completed (True) or incomplete (False)

**Validation Rules**:
- `id` must be a positive integer (auto-incremented from the last used ID)
- `title` must be a non-empty string after stripping whitespace
- `description` can be any string including empty string
- `completed` must be a boolean value (True/False)

**State Transitions**:
- Initial state: `completed = False` (all tasks start as incomplete)
- Transition: `completed = False` → `completed = True` (via mark complete operation)
- Transition: `completed = True` → `completed = False` (via mark complete operation)

## Entity: Task List

**Description**: Collection of Task entities managed by the TodoManager during the session

**Operations**:
- Add new Task objects to the list
- Remove Task objects from the list by ID
- Update existing Task objects by ID
- Retrieve Task objects by ID
- Retrieve all Task objects in the list
- Check if list is empty

**Constraints**:
- Must maintain uniqueness of IDs across all tasks in the list
- Must handle ID gaps (when tasks are deleted, IDs remain constant)
- Must persist in-memory only during the session