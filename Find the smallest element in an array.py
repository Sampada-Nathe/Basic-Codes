""" Find the smallest element in an array
Example 1:
Input: arr[] = {2,5,1,3,0};
Output: 0
"""
arr=list(map(int,input().split()))
arr.sort()
print(arr[0])



