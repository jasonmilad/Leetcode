class Solution:
    def shift(self, nums:List[int]) -> None:
        cin = nums[-1]
        for i in range(len(nums)):
            cout = nums[i]
            nums[i] = cin
            cin = cout

    def rotate(self, nums: List[int], k: int) -> None:
        if k>=len(nums):
            k-=len(nums)
        if k==0:
            return
        else:
            for i in range(k):
                self.shift(nums)
        
        """
        Do not return anything, modify nums in-place instead.
        """