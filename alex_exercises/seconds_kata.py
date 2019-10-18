import sys

def format_duration(seconds):
    time = []
    if not seconds: return "now"

    # years
    years = seconds // 31536000
    if years > 1:
        time.append(str(years) + " years")
    elif years:
        time.append(str(years) + " year")
    seconds = seconds % 31536000
    # days
    days = seconds // 86400
    if days > 1:
        time.append(str(days) + " days")
    elif days:
        time.append(str(days) + " day")
    seconds %= 86400
    # hours
    hours = seconds // 3600
    if hours > 1:
        time.append(str(hours) + " hours")
    elif hours:
        time.append(str(hours) + " hour")
    seconds %= 3600
    # minutes
    minutes = seconds // 60
    if minutes > 1:
        time.append(str(minutes) + " minutes")
    elif minutes:
        time.append(str(minutes) + " minute")
    seconds %= 60
    # seconds
    if seconds > 1:
        time.append(str(seconds) + " seconds")
    elif seconds:
        time.append(str(seconds) + " second")

    if len(time) > 2:
        time = [i + "," for i in time[:-2]] + time[-2:]
        time.insert(-1, "and")
    elif len(time) > 1:
        time.insert(-1, "and")

    return ' '.join(time)

for i in sys.argv[1:]:
	print(format_duration(int(i)))
