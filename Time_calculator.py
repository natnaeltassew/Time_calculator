def add_time(start, duration, day=None):
    # Split start time into time and period (AM/PM)
    time, period = start.split()
    hours, minutes = map(int, time.split(':'))
    add_hours, add_minutes = map(int, duration.split(':'))

    # Add minutes and handle overflow
    minutes += add_minutes
    if minutes >= 60:
        hours += 1
        minutes -= 60

    # Add hours and handle overflow
    hours += add_hours
    days_passed = 0
    while hours >= 12:
        hours -= 12
        if period == "PM":
            days_passed += 1
            period = "AM"
        else:
            period = "PM"

    # Handle the case where hours is 0 (midnight)
    if hours == 0:
        hours = 12

    # Format the new time
    new_time = f"{hours}:{minutes:02d} {period}"

    # Handle the day of the week
    if day:
        day = day.lower().capitalize()
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_index = days_of_week.index(day)
        new_day_index = (day_index + days_passed) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    # Add days passed information
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time


# Test cases
print(add_time("3:54 PM", "4:20"))  # Output: 8:14 PM
print(add_time("11:59 PM", "24:05"))  # Output: 12:04 AM (2 days later)
print(add_time("3:30 PM", "2:12", "Monday"))  # Output: 5:42 PM, Monday
print(add_time("10:10 PM", "3:30"))  # Output: 1:40 AM (next day)
