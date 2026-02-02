# Data Model: Todo Console App - Intermediate Level Features

## Overview
Extended data model for the Todo Console App with priority and tagging capabilities.

## Task Entity

### Fields
| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| id | int | Yes | Auto-generated | Unique auto-incrementing identifier for the task |
| title | str | Yes | N/A | Non-empty string representing the task title |
| description | str | No | "" | String representing the task description (optional) |
| completed | bool | No | False | Boolean indicating whether the task is completed (True) or incomplete (False) |
| priority | str | No | "none" | Priority level: "high", "medium", "low", or "none" |
| tags | list[str] | No | [] | List of string tags for categorizing the task |

### Validation Rules
- `id`: Auto-incremented, must be unique positive integer
- `title`: Must be non-empty after stripping whitespace
- `priority`: Must be one of ["high", "medium", "low", "none"] (case-insensitive input accepted)
- `tags`: List of non-empty strings after trimming whitespace, automatically deduplicated

### State Transitions
- `completed`: Can transition between `True` and `False` via toggle or update operations
- `priority`: Can be changed via update operations from any valid value to any other valid value
- `tags`: Can be modified via update operations, with add/remove/clear operations

## Related Entities

### SearchResult
| Field | Type | Description |
|-------|------|-------------|
| tasks | List[Task] | List of tasks matching the search criteria |
| query | str | The search query that produced these results |

### FilterCriteria
| Field | Type | Description |
|-------|------|-------------|
| status | Optional[str] | Filter by completion status ("complete", "incomplete", "all") |
| priority | Optional[str] | Filter by priority level ("high", "medium", "low", "none") |
| tags | Optional[List[str]] | Filter by presence of specific tags |

### SortOrder
| Field | Type | Description |
|-------|------|-------------|
| field | str | Field to sort by ("priority", "title", "id") |
| direction | str | Sort direction ("asc", "desc") |

## Relationships
- All fields belong to a single Task entity
- Tags are stored as a list within each Task
- SearchResults, FilterCriteria, and SortOrder are transient objects used for operations