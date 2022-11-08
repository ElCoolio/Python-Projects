import pytz
from datetime import datetime, timezone

utc_dt = datetime.now(timezone.utc)

PST = pytz.timezone('US/Pacific')
IST = pytz.timezone('Asia/Jerusalem')

x = utc_dt.isoformat()
y = utc_dt.astimezone().isoformat()
z = utc_dt.astimezone(PST).isoformat()
t = utc_dt.astimezone(IST).isoformat()

import datetime

i = datetime.datetime.now()

print(i.strftime("%H"))


tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.datetime.now(tz_NY)
print("NY time:", datetime_NY.strftime("%H"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.datetime.now(tz_London)
print("London time:", datetime_London.strftime("%H"))

tz_PL = pytz.timezone('Pacific/Johnston') 
datetime_PL = datetime.datetime.now(tz_PL)
print("Portland time:", datetime_PL.strftime("%H"))
