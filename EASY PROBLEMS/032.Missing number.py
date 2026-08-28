class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual
S=Solution()
print(S.missingNumber([3,0,1]))        