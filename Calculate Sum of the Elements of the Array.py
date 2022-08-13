"""
Calculate Sum of the Elements of the Array
Problem Statement: Given an array, we have to find the sum of all the elements in the array.

Examples:

Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: 15
"""

n=int(input())
arr=list(map(int,input().split()))
print(sum(arr))