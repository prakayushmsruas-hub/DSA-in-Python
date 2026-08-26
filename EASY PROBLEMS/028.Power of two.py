class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n%2!=0 and n!=1:
            return False
            
        x=1    
        while x<=n: 
       
            if x!=n:
                x*=2
            elif x==n:
                return True

        return False         
                 

S=Solution()
print(S.isPowerOfTwo(1))
print(S.isPowerOfTwo(16))
print(S.isPowerOfTwo(3))