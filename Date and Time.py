from datetime import date
from datetime import datetime
from datetime import timedelta

# Get Current date
today = date.today()
print "Today is: ", today, " |  Weekday: ", today.weekday()
print "Date Components: ", today.day, today.month, today.year

# Get Current time
t = datetime.time(datetime.now())
print "the current time is", t

##############
# Formatting #
##############

now = datetime.now()
print now.strftime("%a, %d, %B, y") #abbreviated day, day, Month, year
print now.strftime("%c")
print now.strftime("%x")
print now.strftime("%X")

##############
# Time Delta #
##############
print "One year from now will be: " + str(datetime.now() + timedelta(days=65))
print "in 2 weeks and 3 days will be: " + str(datetime.now() + timedelta(weeks=2, days=3))