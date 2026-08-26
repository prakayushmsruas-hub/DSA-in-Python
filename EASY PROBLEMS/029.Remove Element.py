class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
       
        while left <= right:
            if nums[left]==val and nums[right]!=val:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
            elif nums[left]==val and nums[right]==val:
                right-=1
            else:
                left+=1    
        return left       
S=Solution()                
print(S.removeElement([3,2,2,3],3))            
print(S.removeElement([0,1,2,2,3,0,4,2],2))            