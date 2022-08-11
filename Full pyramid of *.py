print("Enter number")
n= int(input())
for i in range(1,n+1):
  for j in range(1,n):
    print(" ",end=" ")
  n=n-1
  for j in range(1,i*2):
    print("*",end=" ")
  print("\r")
  
  """
  Enter number
5
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * *
"""
