"""

Rearrange array in increasing-decreasing order
Problem Statement: Rearrange the array such that the first half is arranged in increasing order, and the second half is arranged in decreasing order

Examples:

Example 1:
Input: 8 7 1 6 5 9
Output: 1 5 6 9 8 7

"""


arr=list(map(int,input().split()))
n=len(arr)
arr.sort()
arr1=arr[:n//2]

arr2=arr[n//2:]

arr1.sort()
arr2.sort(reverse=True)

print(arr1+arr2)

