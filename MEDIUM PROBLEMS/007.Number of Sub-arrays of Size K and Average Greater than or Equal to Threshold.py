class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """

        window_sum = sum(arr[:k])
        count=0
        average = float(window_sum)/k

        if average >= threshold:
            count+=1

        for right in range(k,len(arr)):
            
            window_sum += arr[right]
            window_sum -= arr[right-k]

            average = float(window_sum)/k

            if average >= threshold:
                count+=1

        return count       