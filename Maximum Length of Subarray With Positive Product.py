# Sliding Window
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_len = 0
        negative_count = 0
        first_negative_index = None
        zero_index = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                negative_count = 0
                first_negative_index = None
                zero_index = i
            elif nums[i] < 0:
                negative_count += 1
                if first_negative_index == None:
                    first_negative_index = i

            if negative_count & 1 == 0:
                max_len = max(max_len, i - zero_index)
            else:
                max_len = max(max_len, i - first_negative_index)

        return max_len



# DFS + Memoization
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        @cache 
        # This decorator is used to implement memoization, which is a technique to cache the results of expensive function calls and reuse them when the same inputs occur again in the future.
        def dfs(i = 0, taking = False, positive = True):
            if i == len(nums):
                return 0 if positive else -math.inf

            # we can never include a 0 in the subarray
            if nums[i] == 0:
                return dfs(len(nums) if taking else i + 1, taking, positive)

            # max length if we include this number in the subarray
            including = dfs(i + 1, True, positive == (nums[i] > 0)) + 1

            # max length if we exclude this number from the subarray
            excluding = dfs(len(nums), True, positive) if taking else dfs(i + 1, False)

            return max(including, excluding)

        return dfs()
