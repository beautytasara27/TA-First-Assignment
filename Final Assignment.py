counting = 1
for i in range(0, 15):
    for x in range(0, counting):
        print("*", end="")
    counting = counting + 1
    print()
print(" "*50)

length = 15
for x in range(1, 16):
    print("*"*length)
    length = length - 1
print(" "*50)


length = 10
for i in range(0, length):
    for j in range(0, length-i-1):
        print(end=" ")
    for j in range(0, i+1):
        print("*", end=" ")
    print()

