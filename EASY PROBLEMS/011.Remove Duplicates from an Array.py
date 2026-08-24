#29-06-2026
"""Write a Python program to remove duplicate elements from an array and print only the distinct elements."""

arr=list(map(int,input("Enter elements of the array:").split()))
if not arr:
    print("Array is empty!")
lst=[]
for num in arr:
    if num not in lst:
        lst.append(num)
print("The array with no duplicate values is:",lst)    
