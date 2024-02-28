# O(mnlogn)

class Solution:    
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        row = [0] * n
        ans = 0
        for i in range(m):
            height = [0] * n
            for j in range(n):
                if matrix[i][j] != 0:
                    height[j] = row[j] + 1
            row = height
            height = sorted(height)
            for j in range(n):
                ans = max(ans, height[j] * (n - j))
        return ans

  # O(mn)
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        towers = [(j, 0) for j in range(n)]
        for i in range(m):
            newtowers = [None] * n
            l, r = 0, n - 1
            for col, h in towers:
                if matrix[i][col]:
                    newtowers[l] = (col, h + 1)
                    l += 1
                else:
                    newtowers[r] = (col, 0)
                    r -= 1
            towers = newtowers
            for j in range(n):
                ans = max(ans, (j+1) * towers[j][1])
        return ans
