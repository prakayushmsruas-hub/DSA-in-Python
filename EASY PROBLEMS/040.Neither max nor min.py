class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum=nums[0]
        minimum=nums[0]

        for num in nums:
            if maximum<num:
                maximum=num
            if minimum>num:
                minimum=num
        for num in nums:
            if num!=maximum and num!=minimum:
                return num
        return -1                        