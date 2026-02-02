# API Contract: Todo Console App - Intermediate Features

## Overview
Contract for the new intermediate-level features in the Todo Console App.

## Task Operations

### Add Task with Priority and Tags
```
Method: add_task(title: str, description: str = "", priority: str = "none", tags: List[str] = [])
Returns: int (task_id)
Errors: ValueError if title is empty or priority is invalid
```

### Update Task with Priority and Tags
```
Method: update_task(task_id: int, title: Optional[str] = None, description: Optional[str] = None,
                   completed: Optional[bool] = None, priority: Optional[str] = None,
                   tags: Optional[List[str]] = None)
Returns: bool (success/failure)
Errors: ValueError if priority is invalid, False if task not found
```

## Search Operations

### Search Tasks by Keyword
```
Method: search_tasks(keyword: str) -> List[Task]
Behavior: Case-insensitive search across title, description, and tags
Returns: List of matching Task objects
```

## Filter Operations

### Filter Tasks by Criteria
```
Method: filter_tasks(status: Optional[str] = None, priority: Optional[str] = None,
                     tags: Optional[List[str]] = None) -> List[Task]
Parameters:
  - status: "complete", "incomplete", or "all" (default: None = all)
  - priority: "high", "medium", "low", "none", or None (default: None = all)
  - tags: List of tags to filter by (default: None = all)
Returns: List of matching Task objects
```

## Sort Operations

### Sort Tasks by Criteria
```
Method: sort_tasks(tasks: List[Task], field: str, direction: str = "asc") -> List[Task]
Parameters:
  - tasks: List of Task objects to sort
  - field: "priority", "title", or "id"
  - direction: "asc" or "desc" (default: "asc")
Returns: New list of Task objects in sorted order
```

## Priority Values
Valid priority values: "high", "medium", "low", "none"

## Validation Rules
- Priority values must be one of the valid options (case-insensitive input accepted)
- Tags must be non-empty strings after trimming
- Task titles must be non-empty