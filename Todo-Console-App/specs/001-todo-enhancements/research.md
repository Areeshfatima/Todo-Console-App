# Research: Todo Console App - Intermediate Level Features

## Overview
Research for implementing intermediate-level features in the Todo Console App including priorities, tags, search, filter, and sort functionality.

## Decision Points and Rationale

### 1. Priority Representation
**Decision**: Use string-based priority values ("high", "medium", "low", "none") rather than an enum
**Rationale**: While enums provide type safety, Python strings are simpler to implement and handle user input variations. The validation requirements can be met with string constants.
**Alternatives considered**:
- Enum class with High, Medium, Low, None values (more type-safe but more complex)
- Integer values (1-4 scale, harder to read)

### 2. Tags Storage Approach
**Decision**: Use a list of strings for tags with automatic deduplication
**Rationale**: Lists provide ordering flexibility and the ability to maintain multiple tags. Deduplication on input keeps the list clean while preserving insertion order.
**Alternatives considered**:
- Set (automatically deduplicates but loses order)
- Tuple (immutable once created)

### 3. Search Scope
**Decision**: Search across title, description, and tags fields for comprehensive results
**Rationale**: Users expect to find tasks regardless of which field contains their search term. This provides the most intuitive search experience.
**Alternatives considered**:
- Title and description only (simpler but less comprehensive)
- Configurable search scope (more complex but flexible)

### 4. Filter/Sort Implementation
**Decision**: Return new filtered/sorted lists rather than modifying original list in-place
**Rationale**: Preserves original data order and allows for chaining operations. Memory overhead is minimal for the expected scale (<1000 tasks).
**Alternatives considered**:
- In-place modification (memory efficient but loses original order)

### 5. Menu Integration Strategy
**Decision**: Separate menu options for search, filter, and sort with clear, intuitive prompts
**Rationale**: Separate options provide clarity and align with user expectations for discrete operations. Chaining can be achieved through consecutive operations.
**Alternatives considered**:
- Combined "View with options" menu (conserves menu space but reduces clarity)

### 6. Input Validation Strategy
**Decision**: Normalize priority inputs to accept multiple formats ('h','high','m','medium','l','low') case-insensitive
**Rationale**: User-friendly approach that accepts common abbreviations while maintaining consistent internal representation.
**Alternatives considered**:
- Exact match only (stricter but less user-friendly)
- Case-sensitive only (simpler but less forgiving)

### 7. Display Format for Enhanced Tasks
**Decision**: Show priority indicators (H/M/L/N) and tags [tag1, tag2] in compact format alongside existing display
**Rationale**: Maintains readability while adding the new information. Compact format prevents excessive line length.
**Alternatives considered**:
- Expanded multi-line format (more readable but uses more screen space)
- Separate display modes (flexible but more complex)

## Implementation Order Recommendation

Based on the feature specification and dependencies:

1. **Phase A**: Extend Task model with priority and tags; update add/update operations
2. **Phase B**: Implement display enhancements and priority/tag handling
3. **Phase C**: Add search functionality with keyword matching
4. **Phase D**: Add filter functionality by status and priority
5. **Phase E**: Add sort functionality by priority and title
6. **Phase F**: Integrate new menu options and CLI flows

This order ensures each foundational element is in place before building upon it, minimizing integration issues.