

days_per_month = {"01" : 31, "02" : 28, "03": 31, "04": 30, "05": 31, "06": 30, "07": 31, "08": 31, "09": 30, "10": 31, "11" : 30, "12": 31}


while True:
    start_date = input("Ввиедите начальную дату в формате ДД.ММ.ГГГГ ->")
    end_date = input("Введите конечную дату в формате ДД.ММ.ГГГГ ->")
    try:
        start_day, start_month, start_year = map(int, start_date.split("."))
        end_day, end_month, end_year = map(int, end_date.split("."))
    except:
        print("Введены некорректные данные")
        continue
    if start_year > end_year:
        print("Начальная дата не может быть более поздней, чем конечная")
        continue
    if start_month > end_month and start_year == end_year:
        print("Начальная дата не может быть более поздней, чем конечная")
        continue
    if start_day > end_day and start_month == end_month and start_year == end_year:
        print("Начальная дата не может быть более поздней, чем конечная")
        continue
    if not (1 <= start_month <= 12 and (start_day <= (29 if ((start_year % 4 == 0 and start_year % 100 != 0) or (start_year % 400 == 0)) else 28) if start_month == 2 else 1 <= start_day <= days_per_month[f"{start_month:02d}"] )):
        print("Введена неверная начальная дата")
    if not (1 <= end_month <= 12 and (end_day <= (29 if ((end_year % 4 == 0 and end_year % 100 != 0) or (end_year % 400 == 0)) else 28) if end_month == 2 else 1 <= end_day <= days_per_month[f"{end_month:02d}"])):
        print("Введена неверная конечная дата")
    else:
        break

days_amount = 0

for year in range(start_year, end_year+1):

    local_start_month = start_month if year == start_year else 1
    local_end_month = end_month if year == end_year else 12
    
    feb = 29 if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) else 28
    
    for month in range(local_start_month, local_end_month + 1):

        days_in_month = feb if month == 2 else days_per_month[f"{month:02d}"]

        if year == start_year and month == start_month:
            days_amount += days_in_month - start_day + 1
        elif year == end_year and month == end_month:
            days_amount += end_day
        else:
            days_amount += days_in_month

print(days_amount)

            
