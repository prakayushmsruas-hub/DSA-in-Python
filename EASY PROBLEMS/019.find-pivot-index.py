class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum=0
        total=sum(nums)
        for i in range(len(nums)):
            right_sum=total-left_sum-nums[i]

            if left_sum==right_sum:
                return i
                
            left_sum+=nums[i] 

        return -1        
S=Solution()