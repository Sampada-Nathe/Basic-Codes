"""Reverse a given Array
Problem Statement: You are given an array. The task is to reverse the array and print it.
Examples:

Example 1:
Input: N = 5, arr[] = {5,4,3,2,1}
Output: {1,2,3,4,5}

"""
arr=list(map(int,input().split()))
print(arr[::-1])
