class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elements={}
        length=len(nums)

        for num in nums:
            if num not in elements:
                elements[num]=1
            else:
                elements[num]+=1
        for num in elements:
            if elements[num]>(length//2):
                return num
                
S=Solution()
print(S.majorityElement([2,2,1,1,1,2,2]))