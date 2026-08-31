class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        window = set()

        for right in range(len(nums)):
            if nums[right] in window:
                return True

            window.add(nums[right])

            if right >= k:
                window.remove(nums[right - k])

        return False
            