hrs = input("Enter Hours:")
rate = input("Enter Rate: ")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()
pay = h * r
print("Pay:", pay)