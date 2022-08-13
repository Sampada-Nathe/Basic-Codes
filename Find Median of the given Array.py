
"""Find Median of the given Array
Problem Statement: Given an unsorted array, find the median of the given array.

Examples:

Example 1:
Input: [2,4,1,3,5]
Output: 3

What is a Median?
Median is defined as the value which is present in the middle for a series of values. Note, in order to find the median of an array of integers, we must make sure they are sorted.
"""
arr=list(map(int,input().split()))
n=len(arr)//2
arr.sort()
print(arr[n])