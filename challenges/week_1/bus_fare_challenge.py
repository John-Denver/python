import datetime

date = datetime.date.today()

weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

dayAsString = datetime.date.today()
asweek = dayAsString.weekday()
day = weekDays[asweek]

print('Date: ' +str(date))
print('Day: ' +str(day))

def ans():
    if day == "Monday":
        print('Fare: 100')
    elif day == "Tuesday":
        print('Fare: 100')
    elif day == "Wednesday":
        print('Fare: 100')
    elif day == "Thursday":
        print('Fare: 100')
    elif day == "Friday":
        print('Fare: 100')

    elif day == "Saturday":
        print('Fare: 60')
    else:
        print('Fare: 80')

ans()

