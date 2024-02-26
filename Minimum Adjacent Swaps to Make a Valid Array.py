# Rearrangement Technique

class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        mi = min(nums)                                     # find minimum
        idx1 = nums.index(mi)                              # locate the first mi from the left side
        
        nums = [nums[idx1]] + nums[:idx1] + nums[idx1+1:]  # make the swaps & update `nums`
        
        mx = max(nums)                                     # find maximum 
        idx2 = nums[::-1].index(mx)                        # locate the first mx from the right side
        return idx1 + idx2                                 # return total swaps needed


# Two pointer

class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        e_max = max(nums)
        e_min = min(nums)

        p1 = -1 # for min
        p2 = n # for max

        for i in range(n):
            if nums[i] == e_min:
                if p1 == -1:
                    p1 = i # p1 will point to the leftmost min
            if nums[i] == e_max:
                p2 = i # p1 will point to the rightmost max
        
        if p1 > p2:
            return n - 1 - p2 + p1 - 1
        else:
            return n - 1 - p2 + p1

