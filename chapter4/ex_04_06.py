#   Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

hrs = input("Enter hours: ")
rate = input("Enter rate: ")

def compute_pay(hrs, rate):
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

compute_pay(hrs, rate)
