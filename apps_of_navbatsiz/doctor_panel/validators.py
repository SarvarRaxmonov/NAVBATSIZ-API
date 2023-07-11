from .utils import correct_time_checker, day_duplicate_check

week_days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def validate_working_schedule(list_of_working_days: list):
    if (
        list_of_working_days is not None
        or day_duplicate_check(list_of_working_days) != False
    ):
        for working_day in list_of_working_days:
            for item in working_day:
                if type(item) == str and item not in week_days:
                    raise ValueError(f"Invalid working day: {item}")
                elif type(item) == list:
                    if False == correct_time_checker(item):
                        raise ValueError(f"Invalid working time: {item}")
    else:
        raise ValueError(f"Invalid Data: {list_of_working_days}")

    return list_of_working_days
