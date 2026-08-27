class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            left=k+1
            right=len(nums)-1
            while left<right:
                if nums[k]+nums[left]+nums[right]==0:
                    ans.append([nums[k],nums[left],nums[right]])
                    left+=1
                    right-=1
                elif nums[k]+nums[left]+nums[right] > 0:
                    right-=1
                else:
                    left+=1
        return ans                

S=Solution()                        
print(S.threeSum([-1,0,1,2,-1,-4]))