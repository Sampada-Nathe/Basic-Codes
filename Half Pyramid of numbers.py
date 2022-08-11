
print("Enter the number of rows")
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end=" ")
    print("\r")
""" 
5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""
