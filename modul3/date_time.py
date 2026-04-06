# import datetime
# now = datetime.datetime.now()
# print(now)

# from datetime import datetime
# current_datetime = datetime.now()
# print(current_datetime.date())
# print(current_datetime.time())

# import datetime
# date_part = datetime.date(1993, 8, 22)
# time_part = datetime.time(17, 00, 00)
# combined_datetime = datetime.datetime.combine(date_part, time_part)
# print(combined_datetime)

# import datetime
# specific_datetime = datetime.datetime(year=2026, month=4, day=4, hour=14, minute=40, second=00)
# print(specific_datetime)

# from datetime import datetime
# now = datetime.now()
# day_of_week = now.weekday()
# print(f"Today: {now} {day_of_week}")

# from datetime import datetime, timedelta
# now = datetime.now()
# future_date = now + timedelta(days=30)
# ordinal_number = now.toordinal()
# print(f"Now is {ordinal_number} day")
# print(future_date)
# timestamp = datetime.timestamp(now)
# print(timestamp)
# timestamp = 1775308043
# dt_object = datetime.fromtimestamp(timestamp)
# print(dt_object)

# from datetime import datetime

# now = datetime.now()

# # Форматування дати і часу
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_date) 

# # Форматування лише дати
# formatted_date_only = now.strftime("%A, %d %B %Y")
# print(formatted_date_only)

# # Форматування лише часу
# formatted_time_only = now.strftime("%I:%M %p")
# print(formatted_time_only)  

# # Форматування лише дати
# formatted_date_only = now.strftime("%d.%m.%Y")
# print(formatted_date_only)

# import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")

# local_time = time.localtime(current_time)
# print(f"Місцевий час: {local_time}")

# import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")

# readable_time = time.ctime(current_time)
# print(f"Читабельний час: {readable_time}")

# import time
# start_time = time.perf_counter()
# for _ in range(1_000_000):
#     pass
# end_time = time.perf_counter()
# execution_time = end_time - start_time
# print(f"Time for play: {execution_time}")

# from datetime import datetime
# my_birthday = datetime(year=1993, month=8, day=22).date()
# print(my_birthday)

