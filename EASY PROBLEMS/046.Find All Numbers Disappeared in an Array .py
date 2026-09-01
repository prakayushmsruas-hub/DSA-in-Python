class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        seen = set(nums)

        ans = []

        for i in range(1, n + 1):
            if i not in seen:
                ans.append(i)

        return ans