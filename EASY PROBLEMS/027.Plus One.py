class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        last=len(digits)-1
        while last>=0:
            if digits[last]<9:
                digits[last]+=1
                return digits

            else:
                digits[last]=0
                last-=1
                
        return [1] + digits

S=Solution()

print(S.plusOne([4,3,2,1]))
print(S.plusOne([9]))
print(S.plusOne([9,9]))
print(S.plusOne([9,9,1]))
print(S.plusOne([1,9,9]))
