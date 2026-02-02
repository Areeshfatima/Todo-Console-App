# Console Todo App

A simple command-line interface (CLI) application for managing todo tasks. Built with Python 3.13+ using only the standard library.

## Features

- Add new tasks with titles and optional descriptions
- View all tasks with their completion status
- Update existing tasks (title and description)
- Delete tasks
- Mark tasks as complete/incomplete
- In-memory storage (no persistence)

## Requirements

- Python 3.13 or higher
- No external dependencies (uses only Python standard library)

## Usage

To run the application:

```bash
python3 src/main.py
```

Follow the on-screen menu prompts to manage your tasks:

1. **Add Task**: Create a new task with a title and optional description
2. **View Task List**: See all tasks with their completion status
3. **Update Task**: Modify an existing task's title or description
4. **Delete Task**: Remove a task from the list
5. **Mark as Complete**: Toggle a task's completion status
6. **Exit**: Close the application

## Project Structure

- `src/main.py`: Main CLI interface with menu-driven interaction
- `src/todo_manager.py`: Business logic for task management
- `src/models.py`: Data model definition for Task objects
- `test_todo_app.py`: Comprehensive test suite for all functionality

## Architecture

- **In-Memory Storage**: Tasks are stored in a list in memory with auto-incrementing IDs
- **Data Validation**: Task titles must be non-empty after trimming whitespace
- **Clean Separation**: Models, business logic, and presentation layers are separated
- **Standard Library Only**: No external dependencies for simplicity and portability

## Testing

Run the comprehensive test suite:

```bash
python3 test_todo_app.py
```

The test suite covers all functionality including edge cases and error conditions.