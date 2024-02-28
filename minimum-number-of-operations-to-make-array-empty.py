# First Hashmap Approach
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        out = {}
        for i in nums:
            out[i] = out.get(i,0) + 1
        val = 0
        for i,j in out.items():
            if j==1:
                return -1
            else:
                if j%3==2:
                    val = val + (j//3) + 1
                elif j%3==1:
                    val = val + ((j-4)//3) + 2
                else:
                    val = val + (j//3)
        return val

# Second hashmap apporach

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        operation_count = 0
        for num, freq in counter.items():
            if freq == 1: return -1
            operation_count += freq//3
            if freq % 3 != 0:
                operation_count += 1
        return operation_count

#Max heap Approach

from collections import defaultdict
import heapq

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        maxHeap = list(freq.values())
        heapq.heapify(maxHeap)
        print(maxHeap)
        print(freq)

        ans = 0
        while maxHeap:
            remain = heapq.heappop(maxHeap)
            if remain == 3 or remain >= 3+2:
                remain -= 3
            elif remain >= 2:
                remain -= 2

            if remain == 1:
                return -1

            ans += 1
            if remain > 1:
                heapq.heappush(maxHeap, remain)
            
        return ans




