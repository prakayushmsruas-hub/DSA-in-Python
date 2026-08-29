class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq={}
        unique={}
        for ch in s:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]+=1
        for ch in freq:
            if freq[ch]==1:
                unique[ch]=1
        for ch in range(len(s)):
            if s[ch] in unique:
                return ch                     
        return -1        
S=Solution()
print(S.firstUniqChar("leetcode"))    
print(S.firstUniqChar("l"))    
print(S.firstUniqChar("loveleetcode"))    
print(S.firstUniqChar("aabbb"))    