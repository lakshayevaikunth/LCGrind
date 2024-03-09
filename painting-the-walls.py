# Recursion with backtracking

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        
        def dfs(i, t):
            if t <= 0:  # Base case: no more time left
                return 0
            if i == n:  # Base case: all walls painted
                return float('inf')
            
            # Recursive calls:
            # 1. Skip painting the current wall
            # 2. Paint the current wall if enough time is available
            return min(dfs(i + 1, t), dfs(i + 1, t - time[i] - 1) + cost[i])
        
        # Start the recursion from the first wall with `n` units of time available
        return dfs(0, n)


# DP with Tabulation

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        s = sum(cost)
        dp = [s for _ in range(n + 1)]  # Initialize dp with maximum cost
        dp[0] = 0  # Base case: No cost to paint 0 walls
        
        for i in range(n):  # Iterate over each wall
            time[i] += 1  # Increment time to consider total time needed
            for t in range(n, 0, -1):  # Iterate over possible remaining time in reverse
                x = max(t - time[i], 0)  # Calculate previous time after painting current wall
                dp[t] = min(dp[t], dp[x] + cost[i])  # Update min cost for current time
            
        return dp[-1]  # Return min cost to paint all walls within given time constraint
