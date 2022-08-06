""" Example 1:
Input: [1,2,4,7,7,5]
Output: Second Smallest : 2
	    Second Largest : 5
"""
arr=list(map(int,input().split()))
arr.sort()
new_set=set(arr)
new_list=list(new_set)
print("Second Smallest : ",new_list[1])
print("Second Largest : ",new_list[-2])




