#29-06-2026 DSA:Arrays

"""Write a Python program to find the second smallest distinct element in an array of integers.

   """

arr = list(map(int, input("Enter the elements of array: ").split()))

smallest = arr[0]
second_smallest = float('inf')

for i in range(len(arr)):
    if arr[i] < smallest:
        second_smallest = smallest
        smallest = arr[i]

    elif arr[i] < second_smallest and arr[i] != smallest:
        second_smallest = arr[i]

if second_smallest == float('inf'):
    print("No second smallest element exists.")
else:
    print("Second smallest element:", second_smallest)

