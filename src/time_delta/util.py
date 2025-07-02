from datetime import datetime

def time_delta(t1, t2):
    format_str = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, format_str)
    dt2 = datetime.strptime(t2, format_str)
    delta = abs((dt1 - dt2).total_seconds())
    return str(int(delta))
