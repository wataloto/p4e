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

# total = 0
# for i in a:
#     total = total + i
# print(total)

total = sum(a)
print(total)

count = 0
for i in a:
    count = count + 1
print(count)

average = total / count
print(average)