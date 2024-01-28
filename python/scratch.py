import datetime
from dateutil.relativedelta import relativedelta, MO, TU

dt = datetime.datetime.today().date()


#delta = relativedelta(weekday = MO(-1))

for i in range(1, 13):
	
	delta = relativedelta(month= i, day = 32, weekday = MO(-1))
	print(dt + delta)



