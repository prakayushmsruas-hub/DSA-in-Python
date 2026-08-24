# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 return [i,j]

# print(two_sum([2, 7, 11, 15], 9))
# print(two_sum([3, 2, 4], 6))
# print(two_sum([3, 3], 6))


def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        needed = target - nums[i]
        if needed in seen:
            return [seen[needed], i]
        seen[nums[i]] = i


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))

