#!/usr/bin/env python3
"""
Test script for the Console Todo App functionality.
This script tests all the implemented features without requiring interactive input.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.todo_manager import TodoManager
from src.models import Task


def test_add_task():
    """Test adding tasks functionality."""
    print("Testing Add Task functionality...")
    manager = TodoManager()

    # Add a task
    task_id = manager.add_task("Test Task", "This is a test task")
    assert task_id == 1, f"Expected task ID 1, got {task_id}"

    # Verify the task was added
    tasks = manager.get_all_tasks()
    assert len(tasks) == 1, f"Expected 1 task, got {len(tasks)}"
    assert tasks[0].id == 1, f"Expected task ID 1, got {tasks[0].id}"
    assert tasks[0].title == "Test Task", f"Expected title 'Test Task', got {tasks[0].title}"
    assert tasks[0].description == "This is a test task", f"Expected description 'This is a test task', got {tasks[0].description}"
    assert tasks[0].completed == False, f"Expected completed False, got {tasks[0].completed}"

    print("✓ Add Task functionality works correctly")


def test_view_tasks():
    """Test viewing tasks functionality."""
    print("Testing View Tasks functionality...")
    manager = TodoManager()

    # Add a few tasks
    manager.add_task("First Task", "Description for first task")
    manager.add_task("Second Task", "")

    # Get all tasks
    tasks = manager.get_all_tasks()
    assert len(tasks) == 2, f"Expected 2 tasks, got {len(tasks)}"

    # Check display functionality
    display_output = manager.display_tasks()
    assert "First Task" in display_output, "First Task should be in display output"
    assert "Second Task" in display_output, "Second Task should be in display output"
    assert "[ ]" in display_output, "Should show incomplete status"

    print("✓ View Tasks functionality works correctly")


def test_update_task():
    """Test updating tasks functionality."""
    print("Testing Update Task functionality...")
    manager = TodoManager()

    # Add a task
    task_id = manager.add_task("Original Title", "Original Description")

    # Update the task
    success = manager.update_task(task_id, title="Updated Title", description="Updated Description")
    assert success == True, "Update should return True"

    # Verify the update
    task = manager.find_task_by_id(task_id)
    assert task is not None, "Task should exist after update"
    assert task.title == "Updated Title", f"Expected 'Updated Title', got {task.title}"
    assert task.description == "Updated Description", f"Expected 'Updated Description', got {task.description}"

    # Test updating only completion status
    success = manager.update_task(task_id, completed=True)
    assert success == True, "Update should return True"
    task = manager.find_task_by_id(task_id)
    assert task.completed == True, f"Expected completed True, got {task.completed}"

    print("✓ Update Task functionality works correctly")


def test_delete_task():
    """Test deleting tasks functionality."""
    print("Testing Delete Task functionality...")
    manager = TodoManager()

    # Add a few tasks
    task_id_1 = manager.add_task("Task 1", "Description 1")
    task_id_2 = manager.add_task("Task 2", "Description 2")

    # Verify both tasks exist
    tasks = manager.get_all_tasks()
    assert len(tasks) == 2, f"Expected 2 tasks initially, got {len(tasks)}"

    # Delete one task
    success = manager.delete_task(task_id_1)
    assert success == True, "Delete should return True"

    # Verify only one task remains
    tasks = manager.get_all_tasks()
    assert len(tasks) == 1, f"Expected 1 task after deletion, got {len(tasks)}"

    # Verify the remaining task is the second one
    assert tasks[0].id == task_id_2, f"Expected remaining task ID {task_id_2}, got {tasks[0].id}"

    # Try to delete a non-existent task
    success = manager.delete_task(999)
    assert success == False, "Deleting non-existent task should return False"

    print("✓ Delete Task functionality works correctly")


def test_toggle_complete():
    """Test toggling task completion functionality."""
    print("Testing Toggle Complete functionality...")
    manager = TodoManager()

    # Add a task
    task_id = manager.add_task("Toggle Task", "Task for testing toggle")

    # Initially should be incomplete
    task = manager.find_task_by_id(task_id)
    assert task.completed == False, f"Expected initially incomplete, got {task.completed}"

    # Toggle to complete
    success = manager.toggle_complete(task_id)
    assert success == True, "Toggle should return True"
    task = manager.find_task_by_id(task_id)
    assert task.completed == True, f"Expected now complete, got {task.completed}"

    # Toggle back to incomplete
    success = manager.toggle_complete(task_id)
    assert success == True, "Toggle should return True"
    task = manager.find_task_by_id(task_id)
    assert task.completed == False, f"Expected now incomplete, got {task.completed}"

    # Try to toggle non-existent task
    success = manager.toggle_complete(999)
    assert success == False, "Toggling non-existent task should return False"

    print("✓ Toggle Complete functionality works correctly")


def test_find_task_by_id():
    """Test finding task by ID functionality."""
    print("Testing Find Task by ID functionality...")
    manager = TodoManager()

    # Add a task
    task_id = manager.add_task("Find Task", "Task for testing find")

    # Find the task
    task = manager.find_task_by_id(task_id)
    assert task is not None, "Task should be found"
    assert task.id == task_id, f"Expected task ID {task_id}, got {task.id}"

    # Try to find non-existent task
    task = manager.find_task_by_id(999)
    assert task is None, "Non-existent task should return None"

    print("✓ Find Task by ID functionality works correctly")


def test_validation():
    """Test input validation functionality."""
    print("Testing Input Validation functionality...")
    manager = TodoManager()

    # Test adding task with empty title (should raise ValueError)
    try:
        manager.add_task("")
        assert False, "Should have raised ValueError for empty title"
    except ValueError:
        pass  # Expected

    try:
        manager.add_task("   ")  # Only whitespace
        assert False, "Should have raised ValueError for whitespace-only title"
    except ValueError:
        pass  # Expected

    # Test updating task with empty title (should raise ValueError)
    task_id = manager.add_task("Valid Task", "Valid description")
    try:
        manager.update_task(task_id, title="")
        assert False, "Should have raised ValueError for empty title update"
    except ValueError:
        pass  # Expected

    try:
        manager.update_task(task_id, title="   ")  # Only whitespace
        assert False, "Should have raised ValueError for whitespace-only title update"
    except ValueError:
        pass  # Expected

    print("✓ Input Validation functionality works correctly")


def run_all_tests():
    """Run all tests."""
    print("Running all tests for Console Todo App...\n")

    test_add_task()
    test_view_tasks()
    test_update_task()
    test_delete_task()
    test_toggle_complete()
    test_find_task_by_id()
    test_validation()

    print("\n🎉 All tests passed! The Console Todo App functionality is working correctly.")


if __name__ == "__main__":
    run_all_tests()