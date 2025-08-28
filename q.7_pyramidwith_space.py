n=int(input("enter the number of rows  :"))
for i in range(n):
    for j  in range(n-i-1):
        print("_",end=" ")
    for j in range(2 * i+1):
        print("*",end=" ")
    print()