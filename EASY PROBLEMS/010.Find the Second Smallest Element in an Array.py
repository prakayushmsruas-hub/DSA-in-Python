#29-06-2026 DSA:Arrays

"""Write a Python program to find the second smallest distinct element in an array of integers.

   """
def second_smallest(arr):
    smallest = arr[0]
    second_smallest = None
    for num in arr:
        if num < smallest:
            second_smallest = num
            smallest = num
        elif num != smallest and (second_smallest == None or num < second_smallest):
            second_smallest = num
    return second_smallest

print(second_smallest([847, 213, 956, 421, 78, 634, 129, 502, 771, 345, 918, 267, 54, 689, 432, 105, 823, 376, 591, 244]))
