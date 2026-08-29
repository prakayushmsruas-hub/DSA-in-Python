class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        freq={}
        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
        for num in freq:
            if freq[num]>len(nums)//3:
                ans.append(num)            
        return ans        
S=Solution()
print(S.majorityElement([3,2,3]))        