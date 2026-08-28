class Solution(object):
    def productExceptSelf(self, nums):
        answer = []
        left = 1

        for i in range(len(nums)):
            answer.append(left)
            left *= nums[i]

        right = 1

        for i in range(len(nums)-1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer
        
S=Solution()
print(S.productExceptSelf([1,2,3,4]))        
print(S.productExceptSelf([-1,1,0,-3,3]))        