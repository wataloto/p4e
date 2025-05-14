#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
hrs = input("Enter hours: ")
rate = input("Enter rate: ")

try:
    h = float(hrs)
    r = float(rate)
    if h > 40:
        overtime_hrs = h - 40.0
        overtime_rate = r * 1.5
        pay = (40.0 * r) + (overtime_hrs * overtime_rate)
        print ("Pay:", pay)
    else:
        pay = h * r
        print ("Pay:", pay)
except:
    print("Error, please enter numeric input")
