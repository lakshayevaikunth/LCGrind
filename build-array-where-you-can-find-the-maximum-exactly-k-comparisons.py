# Recursion

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        def helper(i, n, m, k):
            ans = 0
            if n <= 0:
                if k == 0:
                    return 1
                return 0
            for j in range(1, m + 1):
                if j > i:
                    if n >= 1 and k >= 1:
                        ans += helper(j, n - 1, m, k - 1)
                else:
                    if n >= 1:
                        ans += helper(i, n - 1, m, k)
            return ans

        return helper(0, n, m, k)


# memoization
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        def helper(i, n, m, k, dp):
            ans = 0
            mod = 10**9 + 7
            if n <= 0:
                if k == 0:
                    return 1
                return 0
            if dp[n][i][k] != -1:
                return dp[n][i][k]
            for j in range(1, m + 1):
                if j > i:
                    if n >= 1 and k >= 1:
                        ans = (ans + helper(j, n - 1, m, k - 1, dp)) % mod
                else:
                    if n >= 1:
                        ans = (ans + helper(i, n - 1, m, k, dp)) % mod
            dp[n][i][k] = ans % mod
            return dp[n][i][k]

        dp = [[[-1] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        return helper(0, n, m, k, dp)

# Tabulation
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        # Initialize dp table
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

        for j in range(1, m + 1):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(1, m + 1):
                for l in range(1, k + 1):
                    dp[i][j][l] = (dp[i][j][l] + dp[i - 1][j][l] * j) % MOD
                    for num in range(1, j):
                        dp[i][j][l] = (dp[i][j][l] + dp[i - 1][num][l - 1]) % MOD

        result = sum(dp[n][j][k] for j in range(1, m + 1)) % MOD

        return result
