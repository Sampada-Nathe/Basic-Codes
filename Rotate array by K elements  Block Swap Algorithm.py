"""
Rotate array by K elements : Block Swap Algorithm
In this article we will learn a very popular algorithm for “Rotate array by K elements : Block Swap Algorithm”.

Problem Statement: Given an array of n size, rotate the array by k elements using the Block Swap Algorithm.

Examples:

Example 1:
Input: N = 5, array[] = {1,2,3,4,5} K=2
Output: {3,4,5,1,2}
"""
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
print(arr[k:]+arr[:k])
