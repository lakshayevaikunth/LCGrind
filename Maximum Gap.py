# Bucket approach

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0 #edge case 
        mn, mx = min(nums), max(nums)
        step = max(1, (mx - mn)//(len(nums)-1)) #n-1 holes 
        size = (mx - mn)//step + 1
        buckets = [[inf, -inf] for _ in range(size)]
        
        for num in nums: 
            i = (num - mn)//step
            x, xx = buckets[i]
            buckets[i] = min(x, num), max(xx, num)
        
        ans = 0
        prev = mn
        for i in range(size):
            x, xx = buckets[i]
            if x < inf:
                ans = max(ans, x - prev)
                prev = xx 
        return ans 

# Sorting approach

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        nums.sort()
        max_diff=0
        for i in range(len(nums)-1):
            max_diff=max(max_diff,nums[i+1]-nums[i])
        return max_diff
