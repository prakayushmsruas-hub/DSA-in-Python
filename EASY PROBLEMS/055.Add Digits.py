class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            total=0
            while num > 0:
                total+=num%10
                num//=10
            num=total
        return num        