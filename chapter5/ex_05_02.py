a = []
x = input("Enter a number: ")

while x != 'done':
    try:
        x = int(x)
        a.append(x)
    except:
        print("invalid input")  
    x = input("Enter a number: ")

print(a)

smallest = None
for i in a:
    if smallest is None or smallest > i:
        smallest = i
print(smallest)

# smallest = min(a)
# print("The smallest is: ", smallest)

largest = None
for i in a:
    if largest is None or largest < i:
        largest = i
print(largest)

# largest = max(a)
# print("The largest is: ",largest)