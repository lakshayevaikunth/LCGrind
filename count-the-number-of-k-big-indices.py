# Two Sorted Lists
from sortedcontainers import SortedList
class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        sl1,sl2 = SortedList(),SortedList(nums)
        res = 0
        for i in range(len(nums)):
            sl2.remove(nums[i])
            if sl1.bisect_left(nums[i])>=k and sl2.bisect_left(nums[i])>=k:
                res+=1
            sl1.add(nums[i])
        return res


# Two heap approach

class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int :
        # get length of nums 
        numsL = len(nums)
        # if length is not enough to split evenly no good -> return 0 
        if numsL < k * 2 + 1:
            return 0
        # build a left and right max heap for the split of length nums 
        # this lets us find the sorted form without having to sort 
        # and allows us to utilize the binary indexed tree nature without having to make one 
        left_max_heap = []
        right_max_heap = []
        # a value is only valid if on the left if it is > current k largest 
        # we then add this to result if and only if that occurs as well on the right in reverse
        is_valid = [False]*numsL
        result = 0 


        # build left and right max heaps as BIT 
        for index in range(k) : 
            heapq.heappush(left_max_heap,  -nums[index])
            heapq.heappush(right_max_heap, -nums[numsL - 1 - index])

        # explore the range from left to right 
        for index in range(k, numsL-k) : 
            # get current largest on left 
            peak = -left_max_heap[0]
            # if nums at index gt left largest, this is valid 
            # this is valid as thre exists at least k indices (via heap form) 
            # that are smaller than this value and this index is greater than those ones 
            if nums[index] > peak : 
                is_valid[index] = True
            else : 
                # otherwise, if this is not valid, we need to update our heap by popping off current 
                # largest and placing this item in its stead 
                heapq.heapreplace(left_max_heap, -nums[index])
        
        # explore the range from right to left going backwards 
        for index in range(numsL - k - 1, k-1, -1) : 
            # get current largest on right 
            peak = -right_max_heap[0]
            # if nums[index] gt largest on right, we satisfy right condition 
            if nums[index] > peak : 
                # so we increment by whether or not we satisfied left condition 
                result += int(is_valid[index])
            else : 
                # otherwise, we update 
                heapq.heapreplace(right_max_heap, -nums[index])
        
        # at end, return the result of the number of left and right matches 
        return result 
