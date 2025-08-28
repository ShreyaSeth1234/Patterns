n=int(input("enter the number of rows :"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if (j%2==0):
            print("*", end=" ")
        else:
            print(j,end=" ")
    print()       
    