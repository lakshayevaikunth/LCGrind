# Recursion with Memoization - Top Down

class Solution:
    def countOrders(self, n: int) -> int:
        memo = {}
        mod = 10**9 + 7
        def dfs(pickup,delivery):
            if (pickup,delivery) in memo:
                return memo[(pickup,delivery)]
            if pickup == 0:
                return factorial(delivery)
            if pickup > delivery:
                return 0
            memo[(pickup,delivery)] = (pickup*dfs(pickup-1,delivery) + (delivery-pickup)*dfs(pickup,delivery-1)) % mod
            return memo[(pickup,delivery)]
        return dfs(n,n)
      
# Tabulation - Bottom Up
class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        dp =  [0] * (n+1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i-1] * (2 * i - 1) * i
            dp[i] %= MOD

        return dp[n]






