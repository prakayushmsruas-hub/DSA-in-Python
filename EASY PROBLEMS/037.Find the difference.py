class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        prev={}
        new={}
        
        for ch in s:
            if ch not in prev:
                prev[ch]=1
            else:
                prev[ch]+=1
        for ch in t:
            if ch not in new:
                new[ch]=1
            else:
                new[ch]+=1
        for ch in new:
            if ch not in prev or new[ch]>prev[ch]:
                return ch       
                           
S=Solution()
print(S.findTheDifference("a","aa"))        