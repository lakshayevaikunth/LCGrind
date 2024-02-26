# First Approach

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        res = 1
        for i in range(1,len(arr)):
            if (arr[i] > res):
                res += 1
        return res

#Second Approach - Bucketing or PigeonHole Principle

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        buckets = [0] * (n + 1)
        
        for num in arr:
            buckets[min(num, n)] += 1
        
        miss = 0
        for i in range(1, n + 1):
            if buckets[i] == 0:
                miss += 1
            else:
                miss -= min(buckets[i] - 1, miss)
        
        return n - miss
