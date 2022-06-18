
# Return total seconds into their respective hour:minute:seconds


def get_time(seconds):
    hour = seconds//3600
    remainder = seconds % 3600
    minute = remainder//60
    sec = remainder % 60
    return f"{hour}hr :{minute}min :{sec}sec"


print(get_time(132668071))
