# 26-June-2026 -> DSA:Arrays
# count even and odd numbers in an array
"""Write a program that takes an array of integers as input and counts how many odd numbers are present
   in the array.Finally, print both counts

   Time Complexity: O(n)
   
   """

# Input of the list
arr=list(map(int,input("Enter the elements in the list each seperated by space:").split()))

#Initialize even count and odd count to zero
even_count=0
odd_count=0

# traversing
for nums in arr:
    if nums%2==0:
        even_count+=1
    else:
        odd_count+=1    
print(f"The number of elements that are even are {even_count}.\nThe number of elements that are odd are {odd_count}.")   
