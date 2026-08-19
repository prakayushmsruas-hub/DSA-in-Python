# 27-June-2026 -> DSA:Arrays
# Count the frequency of a number
"""You are given an array of integers and a target number. Your task is to count how many times
   the target number appears in the array and display its frequency.
   
   Time Complexity: O(n)
   """
try:
    # Taking input of array
    arr=list(map(int,input("Enter the elements of an array seperated by a space:").split()))
    #Initialize count to zero
    count=0
    if not arr:
        print("The array is empty!")
    else:
        target=int(input("Enter the element for which you want to count the frequency:"))
        for index in range(len(arr)):
            if arr[index]==target:
                count+=1
        print(f"the number {target} appears {count} times")
except ValueError:
    print("Invalid Input\nEnter integers only!")
    