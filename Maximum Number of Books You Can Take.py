# Monotonic Stack Technique - Optimized

class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i, n):
                min_height = min(books[i:j+1])
                width = j - i + 1
                dp[i][j] = (2 * min_height - (width - 1)) * width // 2
        
        max_value = 0
        for i in range(n):
            for j in range(i, n):
                max_value = max(max_value, dp[i][j])
        
        return max_value

# Recursive depth-first search (DFS) approach with memoization

class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        @cache
        def dfs(index, numPrevBooks):
            if index == n: return 0
            res = 0
            # restart collecting books
            if numPrevBooks == 0:
                res = max(res, 0 + dfs(index + 1, 0))
            # try to collect as many as possible from next shelves
            for numBooks in range(numPrevBooks + 1, books[index] + 1):
                res = max(res, numBooks + dfs(index + 1, numBooks))
            return res
        return dfs(0, 0)
