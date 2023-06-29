class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp_mean = mean(nums[:k])
        max_mean = mean(nums[:k])
        n = len(nums)

        for i in range(n-k):
            temp_mean = temp_mean+(nums[i+k]-nums[i])/k
            max_mean = max(max_mean, temp_mean)
        return max_mean