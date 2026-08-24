# 27-June-2026 -> DSA: Arrays
# reverse an array without using slicing.
"""You are given an array of intergers.Your task is to reverse the elements of the array without using 
   python's built-in methods such as [::-1] , reverse() or reversed().
   
   Time Complexity: O(n)
   """
try:
    arr=list(map(int,input("Enter the elements in the array each seperated by a space:").split()))
    if not arr:

        print("Array is Empty!")

    else:

        length=len(arr)
        #starting index
        pointer_1 = 0
        #ending index
        pointer_2 = length-1
        
        while pointer_2>pointer_1:
            #Swapping
            arr[pointer_1],arr[pointer_2]=arr[pointer_2],arr[pointer_1]
            pointer_1+=1
            pointer_2-=1    
        print(f"The reversed array is {arr}")    
except ValueError:
    print("Invalid Input!\nEnter a integer only")        
    