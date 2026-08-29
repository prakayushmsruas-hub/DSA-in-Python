class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
S=Solution()
print(S.intersection([1,2,2,1],[2,2]))    