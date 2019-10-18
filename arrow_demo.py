import arrow


d = arrow.get()
print(d)

next_week = d.shift(days=+7)
print(next_week.humanize())
