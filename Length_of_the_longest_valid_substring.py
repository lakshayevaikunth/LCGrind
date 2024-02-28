# Sliding Window with Two pointers
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        setF=set(forbidden)
        res=left=0
        for i in range (len(word)):
            for j in range (max(left,i-9),i+1):
                if word[j:i+1] in setF:
                    left=j+1
            res=max(res,i-left+1)
        return res


# Trie approach

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        trie = {}
        for f in forbidden:
            t = trie
            for c in f:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t["end"] = True
        
        def isForbidden(s):
            t = trie
            counter = 0
            for c in s:
                if c not in t:
                    return False
                t = t[c]
                counter += 1
                if "end" in t:
                    return counter
            return False
        
        res = 0
        j = len(word)
        for i in range(len(word) - 1, -1, -1):
            truc = isForbidden(word[i:j])
            if truc:
                j = i + truc - 1
            res = max(res, j - i)
        return res
