# O(N*M)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            d[tuple(count)].append(s)

        return d.values()
      
# O(N * K * log K)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for s in strs:
            words[tuple(sorted(s))].append(s)
        return list(words.values())


