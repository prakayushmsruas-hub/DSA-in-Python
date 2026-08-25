class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen={}
        for num in nums:
            if num not in seen:
                seen[num]=1
            elif num in seen:
                seen[num]+=1   
        for count in seen:
            if seen[count]>1:
                return True
        return False     
S=Solution()       
print(S.containsDuplicate([1,2,3,1]))
print(S.containsDuplicate([1,2,3,4]))