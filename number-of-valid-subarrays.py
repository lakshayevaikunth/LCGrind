# Two Pointer Brute Force

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        output = 0

        for i in range(len(nums)):
            j = i + 1
            while j < len(nums) and nums[i] <= nums[j]:
                output += 1
                j += 1
        return output + len(nums)

# Montonic stack

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        ans, stack = 0, []
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] > n:
                stack.pop()
            stack.append(i)
            ans += len(stack)
        return ans

