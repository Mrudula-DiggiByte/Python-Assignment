import calendar

def get_weekday_name(month, day, year):
    weekday_index = calendar.weekday(year, month, day)
    weekdays = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    return weekdays[weekday_index]
