from datetime import datetime

def format_date(date: datetime) -> str:
    return date.strftime("%Y-%m-%d %H:%M:%S")

def calculate_average(grades: list[int]) -> float:
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)
