
# Boundary Value Approach
class Solution(object):
    def sumSubarrayMins(self, arr):
        l = [0] * len(arr)
        for i in range(len(arr)):
            l[i] = i - 1
            while l[i] > -1 and arr[i] < arr[l[i]]: l[i] = l[l[i]]

        r = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            r[i] = i + 1
            while r[i] < len(arr) and arr[i] <= arr[r[i]]: r[i] = r[r[i]]

        res, m = 0, 10**9 + 7
        for i in range(len(arr)):
            res = (res + (i - l[i]) * (r[i] - i) * arr[i]) % m

        return res

# Monotonic Stack
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)
        stack = []
        i = 0
        result = 0
        while i < len(arr):
            current = arr[i]
            countPrev = 1
            while len(stack) and stack[-1][0] >= current:
                topNum, topCountPrev = stack.pop()
                result += topNum * topCountPrev * countPrev
                countPrev += topCountPrev
            stack.append((current, countPrev))
            i += 1
        return result % (10 ** 9 + 7)

# DP
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        total_sum = 0
        n = len(arr)
        min_vals = [[0] * n for _ in range(n)]
        
        for i in range(n):
            min_vals[i][i] = arr[i]
            total_sum += min_vals[i][i]
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                min_vals[i][j] = min(min_vals[i][j-1], arr[j])
                total_sum += min_vals[i][j]
        
        return total_sum % MOD
