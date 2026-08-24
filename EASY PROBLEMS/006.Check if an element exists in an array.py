# 27-June-2026 -> DSA:Arrays
# Check if an element exists in an array
"""Given an array of integers and a target number,determine whether the target number
   is present in the array  
   
   Input:
       arr=[10,25,30,45,50]
       target=30
   Output:
       30 is present in the array at index 2.  

       Time Complexity: O(n)   
                                                                       """

# Exceptional Handling
try:
    # Taking Input of the list
    arr=list(map(int,input("Enter the elements of array seperated by a space:").split()))
    # Displaying the array
    print(f"The array is {arr}")
    if not arr:

        print("The array is empty!")
    
    else:
        # User choosing a target to search
        target=int(input("Enter the number you want to search:"))
        found=False
        for num_index in range(len(arr)):

            if arr[num_index]==target:

                print(f"Target number {target} found at index {num_index}")
                found=True
                break

        if found==False:

            print(f"Target {target} Not found!")        
except ValueError:
    print("Enter Integers only!")                

