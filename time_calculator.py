def add_time(start, duration, day=None):
    # Extract start time information
    start_time, am_pm = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    # Extract duration time information
    duration_hour, duration_minute = map(int, duration.split(":"))
    # Convert start time to 24-hour clock format
    if am_pm == "PM" and start_hour != 12:
        start_hour += 12
    # Add duration time
    end_minute = (start_minute + duration_minute) % 60
    end_hour = (
        start_hour + duration_hour + (start_minute + duration_minute) // 60
    ) % 24
    # Convert end time back to 12-hour clock format
    if end_hour == 0:
        end_hour = 12
        end_am_pm = "AM"
    elif end_hour < 12:
        end_am_pm = "AM"
    elif end_hour == 12:
        end_am_pm = "PM"
    else:
        end_hour -= 12
        end_am_pm = "PM"
    # Calculate number of days later
    num_days_later = (
        start_hour + duration_hour + (start_minute + duration_minute) // 60
    ) // 24
    # Format output string
    output = f"{end_hour}:{end_minute:02d} {end_am_pm}"
    if day is not None:
        # Get index of given day of week
        weekdays = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        day_index = weekdays.index(day.capitalize())
        # Calculate index of resulting day of week
        result_day_index = (day_index + num_days_later) % 7
        # Add resulting day of week to output string
        output += f", {weekdays[result_day_index]}"
    # Add number of days later to output string
    if num_days_later == 1:
        output += " (next day)"
    elif num_days_later > 1:
        output += f" ({num_days_later} days later)"

    return output
