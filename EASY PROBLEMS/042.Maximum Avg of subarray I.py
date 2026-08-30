class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum=sum(nums[:k])
        max_sum=window_sum

        for right in range(k,len(nums)):
            window_sum+=nums[right]
            window_sum-=nums[right-k]

            max_sum=max(max_sum,window_sum)
        return float(max_sum)/k    