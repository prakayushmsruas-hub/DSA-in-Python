class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans = []

        for k in range(len(nums) - 2):

            if k > 0 and nums[k] == nums[k - 1]:
                continue

            if nums[k] > 0:
                break

            if nums[k] + nums[k + 1] + nums[k + 2] > 0:
                break

            left = k + 1
            right = len(nums) - 1

            while left < right:
                total = nums[k] + nums[left] + nums[right]

                if total == 0:
                    ans.append([nums[k], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return ans
S=Solution()                  
print(S.threeSum([-1,0,1,2,-1,-4]))