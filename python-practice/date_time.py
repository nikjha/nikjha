import datetime
dt = datetime.datetime.now()
print("Defatult Date Time of Local System", dt)

import dateutil.parser
#print("Parsing Date and Time with default ", dateutil.parser.parse(
print("printing today's date  ", datetime.date.today())
#print("Current time ", datetime.time())
import time
print("Local Time", time.localtime())

print ("Formatted TIme", time.strftime("%I:%M:%S", time.localtime()))


from datetime import datetime, timedelta, timezone
JST = timezone(timedelta(hours=+9))
dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo=JST)
print("Print Date with +9hour", dt)
print(JST)
#print(datetime(dt, tzinfo=JST))
print("\nTimezone Details :", dt.tzname())


