import calendar

year = int ( input("Enter the yera :"))
month = int ( input ("Enter the month :"))

cal = calendar.month(year,month)
print(cal)