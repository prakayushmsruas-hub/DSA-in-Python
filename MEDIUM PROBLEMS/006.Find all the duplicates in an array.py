class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]

        if len(nums)==1:
            return ans
            
        
        freq={}

        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1

        for num in freq:
            if freq[num]==2:
                ans.append(num)                
        return ans        