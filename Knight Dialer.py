# Memoization
class Solution:
def knightDialer(self, n: int) -> int:
    neighbors = {1: [8,6], 2: [7,9], 3:[4,8], 4: [3,9,0], 5: [], 6: [7, 1, 0], 7: [6,2], 8: [1,3], 9: [4,2], 0: [4,6]}
    memo = {}

    def solve(start, curr):
        if curr == 1: return 1
        if (start, curr) in memo: return memo[(start, curr)]

        # consider jumping to all possible neighbors
        choices = 0
        for neighbor in neighbors[start]:
            choices += solve(neighbor, curr-1)
        memo[(start, curr)] = choices
        return choices

    res, MOD = 0, (10**9)+7
    # sum the solutions of all n-sized numbers starting from all possible starting locations
    for i in range(10):
        res += solve(i, n)
    return res%MOD
  
# Tabulation

class Solution:
    def knightDialer(self, n: int) -> int:
        neighbors = {1: [8,6], 2: [7,9], 3:[4,8], 4: [3,9,0], 5: [], 6: [7, 1, 0], 7: [6,2], 8: [1,3], 9: [4,2], 0: [4,6]}
        vals = [1]*10
        for _ in range(1,n):
            new_vals = [0]*10
            for num in range(10):
                for neighbor in neighbors[num]:
                    new_vals[num] += vals[neighbor]
            vals = new_vals
        return sum(vals)%(10**9+7)
