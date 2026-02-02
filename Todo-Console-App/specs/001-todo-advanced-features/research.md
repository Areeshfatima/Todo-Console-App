# Research: Todo Console App - Advanced Level Features

## Overview
This research document addresses the technical decisions and investigations needed to implement the advanced features for the Todo Console App: due dates and recurring tasks with console-based reminders.

## Key Technical Decisions

### 1. Date/Time Handling
**Decision**: Use `datetime.datetime` with parsing of common formats
**Rationale**: Using a single datetime object for both date and time provides full timestamp support and simplifies the codebase. This approach allows for both date-only and datetime inputs while maintaining consistency.
**Alternatives considered**:
- Separate date and time fields (would complicate comparisons and storage)
- Unix timestamps (less readable and harder to parse from user input)

### 2. Recurrence Frequencies
**Decision**: Enum with predefined values (None/Daily/Weekly/Monthly)
**Rationale**: Using an enum provides validation and makes it easier to advance dates consistently. It also simplifies the user interface by providing clear, discrete options.
**Alternatives considered**:
- Free-text input (would be difficult to validate and process)
- Custom recurrence rules (too complex for console application)

### 3. Recurrence Trigger
**Decision**: Automatic on mark complete
**Rationale**: This provides an intuitive "done → next instance" flow that matches user expectations. When a user marks a recurring task as complete, they expect a new instance to be created.
**Alternatives considered**:
- Dedicated menu command (would require extra user action)
- Background processing (not feasible for console app without persistence)

### 4. Overdue Reminders
**Decision**: Proactive on app start + in list view
**Rationale**: This ensures users are aware of overdue tasks both when they begin using the app and when viewing their tasks, providing good visibility without being overly intrusive.
**Alternatives considered**:
- Only in list view (might miss users who don't immediately view tasks)
- Popup notifications (not feasible in console environment)

### 5. Due Date Sorting/Filtering
**Decision**: Integrate into existing sort/filter functionality
**Rationale**: This maintains consistency with the existing UI patterns and leverages the already-built infrastructure for sorting and filtering.
**Alternatives considered**:
- Separate sort/filter options (would fragment the user experience)

## Date Parsing Strategy

### Supported Formats
- ISO format: `YYYY-MM-DD` (e.g., 2026-02-01)
- With time: `YYYY-MM-DD HH:MM` (e.g., 2026-02-01 14:00)
- With seconds: `YYYY-MM-DD HH:MM:SS` (e.g., 2026-02-01 14:00:30)

### Implementation Approach
- Use `datetime.strptime()` with multiple format attempts
- Provide clear error messages for invalid formats
- Show examples of valid formats in error messages

## Recurrence Logic

### Date Advancement Rules
- Daily: Add 1 day to current due date
- Weekly: Add 7 days to current due date
- Monthly: Add 1 month to current due date (handle month-end edge cases)

### Month-End Handling
For tasks scheduled on the 29th, 30th, or 31st of a month, the system will advance to the last day of the target month if the target month doesn't have that day (e.g., January 31st → February 28th/29th).

## Overdue Detection

### Algorithm
- Compare task's due_datetime with current system time
- If due_datetime < current time AND task is not completed, mark as overdue
- Use `datetime.now()` for comparison (timezone naive approach as specified)

## Edge Case Handling

### Invalid Date Formats
- Provide clear error messages with examples
- Allow users to retry input
- Use try/catch blocks around date parsing

### Tasks Without Due Dates
- Use `Optional[datetime]` type to handle None values
- Ensure all date operations check for None before processing

### Empty Task Lists
- Ensure all date-related operations handle empty lists gracefully
- Prevent errors when sorting/filtering empty lists

## Backward Compatibility

### Existing Tasks
- New attributes (due_datetime, recurrence) will be None/default for existing tasks
- All existing functionality must continue to work unchanged
- Display logic must handle None values appropriately

## Implementation Order

1. Extend Task model with new attributes
2. Update Add/Update to handle new inputs
3. Implement overdue detection
4. Add recurrence processing
5. Integrate reminders and display enhancements
6. Update sorting/filtering to include new attributes