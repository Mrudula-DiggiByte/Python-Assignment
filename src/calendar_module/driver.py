from src.calendar_module.util import get_weekday_name

if __name__ == '__main__':
    month, day, year = map(int, input("Enter date (MM DD YYYY): ").split())
    result = get_weekday_name(month, day, year)
    print(result)