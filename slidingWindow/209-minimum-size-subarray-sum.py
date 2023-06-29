class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = 0
        sum = 0
        n = len(nums)
        left = 0

        for i in range(n):
            sum += nums[i]
            while sum >= target:
                temp_len = i+1-left
                if min_len == 0:
                    min_len = temp_len
                else: 
                    min_len = min(min_len, temp_len)
                sum -= nums[left]
                left+=1
                
        return min_len
