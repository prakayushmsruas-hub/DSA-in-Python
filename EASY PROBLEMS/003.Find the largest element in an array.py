# 26-June-2026 -> DSA:Arrays
#Find the largest element in an array
"""Write a program that takes an array of integers as input and finds the largest element present
   in the array.Finally print the largest element
   
   Time Complexity:O(n)
                                                                 """

# Input of the list
arr=list(map(int,input("Enter the elements in the list each seperated by space:").split()))

# Initialize Largest to the first element of list
largest_element=arr[0]

for index in range(len(arr)):

    if arr[index]>largest_element:

        largest_element=arr[index] #If the previous element not greater than the next element
                                   #then the new element is largest

print(f"The largest Element in {arr} is {largest_element}")        
