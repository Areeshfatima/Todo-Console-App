"""
Utility functions for the Console Todo App.

This module contains utility functions for date parsing and other helper functions.
"""

from datetime import datetime
from typing import Optional


def parse_date_string(date_str: str) -> Optional[datetime]:
    """
    Parse a date string into a datetime object using common formats.

    Args:
        date_str (str): Date string to parse

    Returns:
        Optional[datetime]: Parsed datetime object or None if parsing fails

    Supported formats:
        - YYYY-MM-DD (e.g., 2026-02-01)
        - YYYY-MM-DD HH:MM (e.g., 2026-02-01 14:00)
        - YYYY-MM-DD HH:MM:SS (e.g., 2026-02-01 14:00:30)
    """
    if not date_str or not isinstance(date_str, str):
        return None

    # Strip whitespace
    date_str = date_str.strip()

    if not date_str:
        return None

    # Define supported date formats in order of preference
    formats = [
        "%Y-%m-%d %H:%M:%S",  # YYYY-MM-DD HH:MM:SS
        "%Y-%m-%d %H:%M",     # YYYY-MM-DD HH:MM
        "%Y-%m-%d",           # YYYY-MM-DD
    ]

    # Try each format
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    # If none of the formats work, return None
    return None


def format_datetime(dt: Optional[datetime]) -> str:
    """
    Format a datetime object into a user-friendly string.

    Args:
        dt (Optional[datetime]): DateTime object to format

    Returns:
        str: Formatted date string in YYYY-MM-DD HH:MM format, or empty string if None
    """
    if dt is None:
        return ""

    return dt.strftime("%Y-%m-%d %H:%M")


def advance_date_by_recurrence(base_date: Optional[datetime], recurrence: str) -> Optional[datetime]:
    """
    Advance a date by the specified recurrence interval.

    Args:
        base_date (Optional[datetime]): Base date to advance
        recurrence (str): Recurrence type ("daily", "weekly", "monthly")

    Returns:
        Optional[datetime]: New date advanced by the recurrence interval, or None if input is None
    """
    if base_date is None:
        return None

    # Convert recurrence to lowercase for comparison
    recurrence_lower = recurrence.lower()

    from datetime import timedelta

    if recurrence_lower == "daily":
        return base_date + timedelta(days=1)
    elif recurrence_lower == "weekly":
        return base_date + timedelta(days=7)
    elif recurrence_lower == "monthly":
        # Handle month advancement with consideration for month lengths
        year = base_date.year
        month = base_date.month

        # Increment month
        month += 1
        if month > 12:
            month = 1
            year += 1

        # Adjust day if it exceeds the number of days in the new month
        day = base_date.day
        max_day_in_month = get_days_in_month(year, month)
        if day > max_day_in_month:
            day = max_day_in_month

        # Create the new date with the adjusted day
        try:
            return base_date.replace(year=year, month=month, day=day)
        except ValueError:
            # This handles edge cases like Feb 29 on non-leap years
            # In case of any error, return None
            return None
    else:
        # If recurrence is not recognized, return None
        return None


def get_days_in_month(year: int, month: int) -> int:
    """
    Get the number of days in a given month.

    Args:
        year (int): Year
        month (int): Month (1-12)

    Returns:
        int: Number of days in the month
    """
    import calendar
    return calendar.monthrange(year, month)[1]


def is_overdue(task_due_datetime: Optional[datetime], current_time: Optional[datetime] = None) -> bool:
    """
    Check if a task is overdue based on its due date.

    Args:
        task_due_datetime (Optional[datetime]): Due date of the task
        current_time (Optional[datetime]): Current time to compare against (defaults to now)

    Returns:
        bool: True if task is overdue, False otherwise
    """
    if task_due_datetime is None:
        return False

    if current_time is None:
        current_time = datetime.now()

    return task_due_datetime < current_time