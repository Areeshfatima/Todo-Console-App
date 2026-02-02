# Tasks: Console Todo App

**Feature**: Console Todo App | **Branch**: `001-console-todo-app` | **Date**: 2026-01-30

**Input**: Implementation plan and feature specification from `/specs/001-console-todo-app/`

## Phase 1: Setup

### Goal
Initialize project structure and foundational elements needed for all user stories.

### Independent Test
Verify that the project structure is in place and basic imports work.

### Tasks
- [x] T001 Create src directory structure
- [x] T002 [P] Create models.py file with Task dataclass definition
- [x] T003 [P] Create todo_manager.py file with TodoManager class skeleton
- [x] T004 [P] Create main.py file with basic CLI structure

## Phase 2: Foundational Elements

### Goal
Implement core components that are required by multiple user stories (Task model and basic TodoManager structure).

### Independent Test
Verify that Task model can be instantiated and TodoManager can be initialized with an empty task list.

### Tasks
- [x] T005 Implement Task dataclass in src/models.py with id, title, description, completed fields
- [x] T006 Add type hints and docstrings to Task class
- [x] T007 Implement TodoManager class with task_list and next_id attributes
- [x] T008 Add methods for getting next available ID and validating inputs

## Phase 3: User Story 1 - Add New Task (Priority: P1)

### Goal
Enable users to create new tasks with a required title and optional description. Each task receives a unique auto-incrementing ID and defaults to incomplete status.

### Independent Test
Can launch the application, select the "Add Task" option, provide a title and description, and verify that the task appears in the task list with a unique ID and incomplete status indicator.

### Acceptance Tests
1. Given user is at the main menu, When user selects "Add Task" and enters a valid title and description, Then the task is added to the list with a unique auto-incrementing ID and incomplete status indicator [ ], and a success message is displayed.
2. Given user is at the "Add Task" prompt, When user enters an empty title, Then the system shows an error message and returns to the task addition prompt without creating a task.

### Tasks
- [x] T009 [US1] Implement add_task method in TodoManager class
- [x] T010 [US1] Add input validation for title (non-empty after stripping whitespace)
- [x] T011 [US1] Implement auto-incrementing ID assignment
- [x] T012 [US1] Set default completed status to False
- [x] T013 [US1] Add error handling for empty title validation
- [x] T014 [US1] Integrate add_task functionality into main.py CLI loop

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

### Goal
Display all tasks in a formatted list showing ID, completion status, title, and description. Handle empty list with friendly message.

### Independent Test
Launch the application and select "View Tasks", verify that all added tasks are displayed with appropriate formatting including ID numbers, status indicators ([ ] or [✓]), titles, and descriptions.

### Acceptance Tests
1. Given user has multiple tasks in the system, When user selects "View Tasks", Then all tasks are displayed with ID, status indicator, title, and description in a clear, organized format.
2. Given user has no tasks in the system, When user selects "View Tasks", Then the system displays a friendly message indicating no tasks exist rather than showing an empty list.

### Tasks
- [x] T015 [US2] Implement get_all_tasks method in TodoManager class
- [x] T016 [US2] Create formatted display function for tasks in TodoManager
- [x] T017 [US2] Add special handling for empty task list
- [x] T018 [US2] Format output with ID, status indicator ([ ]/[✓]), title, and description
- [x] T019 [US2] Integrate view functionality into main.py CLI loop

## Phase 5: User Story 5 - Mark Task Complete/Incomplete (Priority: P1)

### Goal
Allow users to toggle the completion status of tasks by ID. Core functionality for tracking task completion.

### Independent Test
Have a task in the system, select "Mark Complete", provide the valid task ID, and verify the status indicator changes from [ ] to [✓] or vice versa.

### Acceptance Tests
1. Given user has an incomplete task in the system, When user selects "Mark Complete" and provides the valid task ID, Then the task's status indicator changes from [ ] to [✓].
2. Given user attempts to toggle completion status of a non-existent task ID, When user selects "Mark Complete" and enters an invalid task ID, Then the system shows an error message and returns to the main menu without making changes.

### Tasks
- [x] T020 [US5] Implement toggle_complete method in TodoManager class
- [x] T021 [US5] Add task lookup by ID functionality
- [x] T022 [US5] Implement status toggle logic
- [x] T023 [US5] Add error handling for invalid task IDs
- [ ] T024 [US5] Integrate mark complete functionality into main.py CLI loop

## Phase 6: User Story 3 - Update Task Details (Priority: P2)

### Goal
Allow users to modify the title or description of existing tasks by ID, supporting partial updates while maintaining ID and completion status.

### Independent Test
Have a task in the system, select "Update Task", provide a valid task ID, modify either the title, description, or both, then verify the changes are reflected in the task list.

### Acceptance Tests
1. Given user has an existing task with specific title and description, When user selects "Update Task" and provides a valid task ID and new title, Then the task's title is updated while preserving other attributes.
2. Given user attempts to update a non-existent task ID, When user selects "Update Task" and enters an invalid task ID, Then the system shows an error message and returns to the main menu without making changes.

### Tasks
- [ ] T025 [US3] Implement update_task method in TodoManager class
- [ ] T026 [US3] Add support for partial updates (title or description only)
- [ ] T027 [US3] Preserve task ID and completion status during updates
- [ ] T028 [US3] Add input validation for title updates (non-empty if provided)
- [ ] T029 [US3] Add error handling for invalid task IDs
- [ ] T030 [US3] Integrate update functionality into main.py CLI loop

## Phase 7: User Story 4 - Delete Task (Priority: P2)

### Goal
Allow users to permanently remove tasks by specifying their ID. Essential for managing the todo list.

### Independent Test
Have a task in the system, select "Delete Task", provide the valid task ID, and verify the task no longer appears in the task list.

### Acceptance Tests
1. Given user has an existing task in the system, When user selects "Delete Task" and provides a valid task ID, Then the task is removed from the list and a confirmation message is displayed.
2. Given user attempts to delete a non-existent task ID, When user selects "Delete Task" and enters an invalid task ID, Then the system shows an error message and returns to the main menu without making changes.

### Tasks
- [ ] T031 [US4] Implement delete_task method in TodoManager class
- [ ] T032 [US4] Add task lookup and removal by ID
- [ ] T033 [US4] Preserve ID gaps (don't reindex remaining tasks)
- [ ] T034 [US4] Add confirmation message after deletion
- [ ] T035 [US4] Add error handling for invalid task IDs
- [ ] T036 [US4] Integrate delete functionality into main.py CLI loop

## Phase 8: CLI Menu Integration

### Goal
Complete the menu-driven interface with all five core operations and proper navigation flow.

### Independent Test
Verify that all five core operations (Add, View, Update, Delete, Mark Complete) are accessible through the menu-driven interface with clear prompts and navigation.

### Tasks
- [ ] T037 Implement main menu with numbered options (1-6)
- [ ] T038 Add clear prompts for each operation
- [ ] T039 Implement proper input validation and error handling
- [ ] T040 Add graceful exit functionality
- [ ] T041 Test complete menu flow with all operations

## Phase 9: Polish & Cross-Cutting Concerns

### Goal
Implement error handling, input validation, and edge case handling as specified in requirements.

### Independent Test
Verify that all invalid inputs are handled gracefully with clear error messages, and that the system behaves correctly with edge cases.

### Acceptance Tests
1. Verify all invalid inputs (empty titles, non-existent IDs) are handled gracefully with clear error messages.
2. Verify all tasks display with proper formatting including ID numbers, status indicators ([ ], [✓]), titles, and descriptions.
3. Verify system maintains task data consistently in memory throughout the session without corruption.

### Tasks
- [ ] T042 Implement comprehensive error handling throughout application
- [ ] T043 Add input sanitization (strip whitespace)
- [ ] T044 Handle non-numeric task IDs gracefully
- [ ] T045 Test extreme length inputs for titles/descriptions
- [ ] T046 Verify ID gap handling after deletions
- [ ] T047 Add type hints to all functions and methods
- [ ] T048 Add docstrings to all functions and classes
- [ ] T049 Perform final integration testing of all features
- [ ] T050 Verify all constitution requirements are met

## Dependencies

- US1 (Add Task) must be completed before US3 (Update Task) and US4 (Delete Task) can be fully tested
- Foundational elements (Task model, TodoManager structure) must be completed before any user story
- All user stories depend on the basic CLI structure being in place

## Parallel Execution Opportunities

- Task T002-T004 can be executed in parallel (creating the three main files)
- US2 (View Tasks), US3 (Update Task), US4 (Delete Task), and US5 (Mark Complete) can be developed in parallel after US1 (Add Task) and foundational elements are complete

## Implementation Strategy

- **MVP Scope**: Complete Phase 1, 2, and 3 (Task model, TodoManager, Add Task functionality) for minimal working application
- **Incremental Delivery**: Each user story phase adds complete functionality that can be tested independently
- **Cross-cutting**: Final phase addresses all error handling, validation, and polish items across the entire application