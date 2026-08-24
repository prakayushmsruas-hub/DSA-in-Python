# 26-June-2026 -> DSA:Arrays
# Find the smallest element in an array
"""Write a program that takes an array of integers as input and finds the smallest element present
   in the array.Finally print the smallest element
   
   Time Complexity:O(n)
                                                                 """

# Input of the list
arr=list(map(int,input("Enter the elements in the list each seperated by space:").split()))

# Initialize smallest to the first element of list
smallest_element=arr[0]

for index in range(len(arr)):

    if arr[index]<smallest_element:

        smallest_element=arr[index] #If the previous element greater than the next element
                                   #then the new element is smallest

print(f"The smallest Element in {arr} is {smallest_element}")       
