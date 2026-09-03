class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Variable sliding window. 
        left=0
        answer=0
        seen=set()
        for right in range(len(s)):
        
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])    
            answer=max(answer,right-left+1)
        return answer    