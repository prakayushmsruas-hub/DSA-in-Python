class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left=0
        right=len(nums)-1
        arr=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[left])>abs(nums[right]):
                arr[i]=nums[left]**2
                left+=1
            else:
                arr[i]=nums[right]**2
                right-=1
        return arr
S=Solution()     
print(S.sortedSquares([-4,-1,0,3,10]))              