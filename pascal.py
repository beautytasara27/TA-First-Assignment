a = int(input("Input the number of rows"))
my_list =[]
for i in range(0,a):
    my_list.append([])
    my_list[i].append(1)
    for j in range(1, i):
        my_list[i].append(my_list[i-1][j-1]+my_list[i-1][j])
        if(a!=0):
            my_list[i].append(1)
for i in range (a):
    print(" "*(a-1), end=" ",sep=" ")
    for j in range(0, i+1):
        print('{0:6}'.format(a[i][j]),end=" ",sep=" ")

    print()
