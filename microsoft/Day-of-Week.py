"""
Days of the week are represented as 3 letter strings
Given S, representing day of week, and integer K, between 0-500, 
return day of the week that is K days later
"""


def dayOfWeek(s, k):
    days = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
    integers = {y: x for x, y in days.items()}
    return days[(integers[s] + k) % 7]


print(dayOfWeek("Sat", 23))
