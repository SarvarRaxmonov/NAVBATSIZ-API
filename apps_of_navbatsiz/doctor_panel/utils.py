from datetime import datetime as dt
from collections import Counter


def correct_time_checker(working_schedule_time: list):
    time = working_schedule_time
    check = True
    if len(working_schedule_time) in [2, 4]:
        for i in range(len(time) - 1):
            wr_time = [str_time_converter(time[i]), str_time_converter(time[i + 1])]
            if wr_time[0] > wr_time[1]:
                check = False
                break
    else:
        check = False
    return check


def str_time_converter(time: str):
    return dt.strptime(time, "%H:%M").time()


def day_duplicate_check(days: list):
    work_days = [item for schedule in days for item in schedule if type(item) == str]
    check_duplicates = Counter(work_days).most_common(1)
    print(
        check_duplicates,
        "////////////////////////////////////////////////////////////////",
    )
    if check_duplicates[0][1] > 1:
        return False
    return True
