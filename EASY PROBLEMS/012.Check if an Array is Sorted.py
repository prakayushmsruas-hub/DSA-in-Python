#30-6-2026 DSA:Arrays

"""Given an array of integers, determine whether the array is sorted in non-decreasing order (ascending order allowing equal elements).
   """

arr = list(map(int, input("Enter the elements of array: ").split()))

sorted_array = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        sorted_array = False
        break

if sorted_array:
    print("Array is sorted")
else:
    print("Not sorted")