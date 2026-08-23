# 27-June-2026 -> DSA: Arrays
#Find the second largest element in an array
"""You are given an array of integers.Your task is to find the second largest distinct element in the array
   without sorting the array"""

def second_largest(arr):
    largest = arr[0]
    second_largest = None
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num != largest and (second_largest == None or num > second_largest):
            second_largest = num
    return second_largest


print(second_largest([847, 213, 956, 421, 78, 634, 129, 502, 771, 345, 918, 267, 54, 689, 432, 105, 823, 376, 591, 244]))