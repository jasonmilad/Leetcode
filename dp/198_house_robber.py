class Solution:
    def robHelper(self, i: int, nums: List[int], memo: List[int]) -> int:
        if i==len(nums)-1:
            return nums[i]
        elif i>len(nums)-1:
            return 0
        elif memo[i] != None:
            return memo[i]
        else:
            memo[i] = max(nums[i] + self.robHelper(i+2, nums, memo), nums[i+1] + self.robHelper(i+3, nums, memo))
            return memo[i]
            
    def rob(self, nums: List[int]) -> int:
        memo = [None] * len(nums)
        return self.robHelper(0, nums, memo)