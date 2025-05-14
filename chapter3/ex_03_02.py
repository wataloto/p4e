#Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

hrs = input("Enter hours: ")
rate = input("Enter rate: ")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if h > 40:
    overtime_hrs = h - 40.0
    overtime_rate = r * 1.5
    pay = (40.0 * r) + (overtime_hrs * overtime_rate)
    print ("Pay:", pay)
else:
    pay = h * r
    print ("Pay:", pay)
