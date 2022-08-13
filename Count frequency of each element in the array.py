"""Count frequency of each element in the array
Problem statement: Given an array, we have found the number of occurrences of each element in the array.
Examples:

Example 1:
Input: arr[] = {10,5,10,15,10,5};
Output: 10  3
	 5  2
     15  1
"""
arr=list(map(int,input().split()))
dict1={}
for i in arr:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
for x,y in dict1.items():
    print(f"{x} occurs {y} times in the array")
