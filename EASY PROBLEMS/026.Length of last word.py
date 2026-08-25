class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ptr=len(s)-1
        length=0
        
        while ptr>=0 and s[ptr]==' ':
            ptr-=1
            
        while ptr>=0 and s[ptr]!=" ":
            length+=1
            ptr-=1

        return length

S=Solution()                   
print(S.lengthOfLastWord("   fly me   to   the moon  "))