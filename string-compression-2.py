# DFS with memoization

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dfs(pos, k, prev_char, prev_char_cnt):
            if pos == len(s):
                return 0
            skip = inf
            if k > 0:
                skip = dfs(pos+1, k-1, prev_char, prev_char_cnt)
            
            if s[pos] == prev_char:
                char_cnt = prev_char_cnt + 1
            else:
                char_cnt = 1

            if char_cnt == 1 or char_cnt == 2 or char_cnt == 10 or char_cnt == 100:
                add = 1
            else:
                add = 0

            keep = dfs(pos+1, k, s[pos], char_cnt) + add

            return min(keep, skip)
        return dfs(0, k, None, 1)

# DP with Memoization

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        # memo-ing a python way, basically we store the result of the function with these parameters in memory,
        # so if it gets called again with the same parameters, it'll just access it in O(1) time in memory
        # we need to know, which index we're at, the prev character that was included in our run-encoded-string, and the count of it, as well as how many deletes we have left
        @lru_cache(None)
        def dp(i, prev_character, character_count,deletes_left):

            #if we're at the end, we can just return 0, since length of run-encoded string "" is 0
            if i == len(s):
                return 0

            #if our current character is the same as the previous character,
            if s[i] == prev_character:
                #we keep the character, so we don't spend a delete
                keep = dp(i + 1, prev_character, character_count + 1, deletes_left)
                #then we only add 1, if it's gonna increase the number of digits in the count
                if character_count in {1, 9, 99}:
                    keep += 1
            else:
                #if it's a new character, we need to increase the length of our res by 1
                keep = dp(i + 1, s[i], 1, deletes_left) + 1
            #if we have deletes left, we can compare this result if we didn't include this current character
            if deletes_left:
                delete = dp(i + 1, prev_character, character_count, deletes_left - 1)
                #get the smaller of the delete, or not delete
                return min(keep, delete)
            #if we don't have deletes left, we have to just return the keep version
            return keep

        return dp(0, None, 0, k)
