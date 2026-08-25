class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_count=0
        max_count=0
        length=len(nums)
        for i in range(len(nums)):

            if nums[i]==1:
                current_count+=1
                
            else :
                max_count=max(current_count,max_count)
                current_count=0
                
        max_count=max(current_count,max_count)        
        return max_count
S=Solution()                
print(S.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(S.findMaxConsecutiveOnes([1,0,1,1,0,1]))

