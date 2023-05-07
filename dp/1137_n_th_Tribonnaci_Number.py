class Solution:

    def helpTrib(self, n: int, memo: [int]):
        if memo[n] != None:
            return memo[n]
        elif n==0:
            return 0
        elif n==1 or n==2:
            return 1
        memo[n] = self.helpTrib(n-1, memo) + self.helpTrib(n-2, memo) + self.helpTrib(n-3, memo)
        return memo[n]

    def tribonacci(self, n: int) -> int:
        memo = [None] * (n+1)
        return self.helpTrib(n, memo)