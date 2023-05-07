#Time and space complexities: O(n)
#recursion + memoization

class Solution:
    def helpFib(self, n: int, memo: [int]) -> int:
        if memo[n] != None:
            return memo[n]
        elif n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            memo[n] = self.helpFib(n-1, memo) + self.helpFib(n-2, memo)
            return memo[n]

    def fib(self, n: int) -> int:
        memo = [None]*(n+1)
        return self.helpFib(n, memo)