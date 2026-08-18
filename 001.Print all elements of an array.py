# 26-June-2026 -> DSA:Arrays
#Print all elements of an array
"""Write a program that takes an array of integers and prints each element on a seperate line
   Example:
   Input: [10,20,30,40,50]
   Output:
   10
   20
   30
   40
   50  

   time Complexity: O(n) because of loop                                       
                                                             """
# Exceptional Handling
try:
    # Taking Input of list
    arr=list(map(int,input("Enter elements of an array each seperated by a space:").split()))
    
    # Traversing across the list
    for i in range(len(arr)):

        print(arr[i])

except ValueError:
    # Error is handled
    print("Invalid Input!\nEnter integers only")        


