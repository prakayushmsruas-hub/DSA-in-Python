# 26-June-2026 -> DSA:Arrays
#Find the sum of all elements in an array
"""Write a program that takes an array of integers as input and calculates the sum of all
   the elements present in the array.Finally print the sum
   
   Input: 10 20 30 40
   Output: 100

   Time Complexity: O(n)
                                                                     """

#Input a list
arr=list(map(int,input("Enter the elements of the array seperated by a space:").split()))
# Initialize sum to zero
total=0
# Traversing
for nums in arr:
    total+=nums
print(f"Sum of all elements in the list is {total}")    