days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start_date = input("Введите начальную дату в формате ДД.ММ.ГГГГ ->")
end_date = input("Введите конечную дату в формате ДД.ММ.ГГГГ ->")

start_day, start_month, start_year = map(int, start_date.split("."))
end_day, end_month, end_year = map(int, end_date.split("."))

def days_from_zero(day, month, year):
    total = 0
    
    for y in range(1, year):
        total += 366 if (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)) else 365
    
    for m in range(1, month):
        if m == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            total += 29
        else:
            total += days_per_month[m - 1]
    
    total += day
    return total

start_total = days_from_zero(start_day, start_month, start_year)
end_total = days_from_zero(end_day, end_month, end_year)

print(end_total - start_total + 1)