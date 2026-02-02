# Quickstart Guide: Console Todo App

## Setup Instructions

1. Ensure Python 3.13+ is installed on your system
2. Clone or download the repository
3. Navigate to the project root directory
4. Run the application using Python:

```bash
python src/main.py
```

## Getting Started

When you start the application, you'll see a numbered menu with the following options:

1. **Add Task**: Create a new task with a required title and optional description
2. **View Task List**: Display all tasks with ID, status indicator ([ ]/[✓]), title, and description
3. **Update Task**: Modify the title and/or description of an existing task by ID
4. **Delete Task**: Remove a task by its ID
5. **Mark as Complete**: Toggle the completion status of a task by ID
6. **Exit**: Quit the application

## Example Workflow

1. Select option 1 to add a new task
2. Enter a title (required) and description (optional)
3. Select option 2 to view your task list
4. Use other options as needed
5. Select option 6 to exit when done

## Error Handling

- If you enter an empty title when adding/updating, the system will show an error
- If you reference a non-existent task ID, the system will show an error
- Invalid inputs will be handled gracefully with helpful messages

## Features

- In-memory storage (tasks persist only during the session)
- Auto-incrementing task IDs
- Formatted task display with status indicators
- Menu-driven interface for ease of use
- Proper error handling and validation