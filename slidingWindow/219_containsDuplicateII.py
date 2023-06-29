class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #iterate over array, adding onto the hash table *the most recent*      index if the test fails && its already there, otherwise continue
        n = len(nums)
        hash_table = {}

        for j in range(n):
            if nums[j] in hash_table:
                i = hash_table[nums[j]]
                if abs(i - j)<=k:
                    return True
            hash_table[nums[j]] = j
        return False

