# 27-June-2026 -> DSA: Arrays
#Find the second largest element in an array
"""You are given an array of integers.Your task is to find the second largest distinct element in the array
   without sorting the array"""

try:
    arr=list(map(int,input("Enter the elements in the array each seperated by a space:").split()))
    if not arr:

        print("Array is Empty!")

    else:

        largest=arr[0]
        second_largest=float('-inf')

        for index in range(len(arr)):

            if arr[index]>largest:

                second_largest=largest
                largest=arr[index]
                
            elif arr[index]>second_largest and arr[index]!=largest:

                second_largest=arr[index]     

        if largest!=second_largest:

            print(f"The largest element is {largest}") 

            if second_largest!=float('-inf'): 

                print(f"The second largest element is {second_largest}")  
            else:

                print("Second largest element is not in array")        
               

except ValueError:
    print("Enter integers only!")
