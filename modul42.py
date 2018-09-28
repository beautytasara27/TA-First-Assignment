#to input list
a = [int(x) for x in input().split()]
def modulus():
    print(a)
    for i in a:
        y = i % 42
        print(i, " "*20, y)

modulus()
