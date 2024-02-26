# Hash Map + Prefix Sum

Sure, here's the revised version:

# 1. Objective: Find the shortest subarray in the given list.
# 2. Requirement: The sum of the elements in the subarray, when divided by a given number `p`, should leave a specific remainder.
# 3. Approach:
#    - Iterate through the list, calculating the running sum of elements.
#    - Track the remainders obtained when dividing the running sum by `p`.
#    - Use a hash table to store the positions where these remainders occur.
#    - Maintain a prefix sum to efficiently calculate the running sum of elements.
# 4. Finding the Shortest Subarray**:
#    - Whenever a remainder matches the target remainder, calculate the length of the subarray between the current position and the position where the matching remainder was first encountered.
#    - Update the answer to be the minimum of the current answer and the length of this subarray.
# 5. Result:
#    - After iterating through the list, if a valid subarray is found, return the length of that subarray.
#    - If no valid subarray is found, return -1 to indicate impossibility.

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        d = {0:-1}
        size = len(nums)
        need = sum(nums)%p
        cur = 0
        res = len(nums)


       
        for key, val in enumerate(nums):
            cur = (cur+val)%p
            d[cur] = key
            if (cur - need)%p in d:
                res = min(res, key - d[(cur - need) % p]) 

        return -1 if res == len(nums) else res
