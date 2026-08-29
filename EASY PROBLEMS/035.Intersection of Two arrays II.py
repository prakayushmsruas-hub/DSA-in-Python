class Solution(object):
    def intersect(self, nums1, nums2):
        ans = []
        n1 = {}
        n2 = {}

        for num in nums1:
            if num not in n1:
                n1[num] = 1
            else:
                n1[num] += 1

        for num in nums2:
            if num not in n2:
                n2[num] = 1
            else:
                n2[num] += 1

        for num in n1:
            if num in n2:
                times = min(n1[num], n2[num])

                for i in range(times):
                    ans.append(num)

        return ans
S=Solution()
print(S.intersect([1,2,2,1],[2,2]))    