#Time and space complexities: O(n)
#recursion + memoization

class Solution:
    def helper(self, n: int, memo: [int]) -> int:
        if memo[n]!=None:
            return memo[n]
        elif n==1:
            return 1
        elif n==2:
            return 2
        else:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
            return memo[n]

    def climbStairs(self, n: int) -> int:
        memo = [None] * (n+1)
        return self.helper(n, memo)
