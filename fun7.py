
print("Enter the number of rows")
n=int(input())
for i in range(1,n+1):
    for j in range(n-i+1):
        print("*",end=" ")
    print("\r")
