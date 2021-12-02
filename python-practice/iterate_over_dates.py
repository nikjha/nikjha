import datetime
day_delta = datetime.timedelta(days=1)
start_date = datetime.date.today()
end_date = start_date +7*day_delta
print("Printing Dates for next 7 days")
for i in range((end_date - start_date).days):

   print( start_date+i*day_delta)

