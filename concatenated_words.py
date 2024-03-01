# O(n * m)

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Create a set of input words for fast lookup
        words_set = set(words)
    # Initialize an empty list to store concatenated words
        concatenated_words = []

    # Iterate through each word in the input list
        for word in words:
        # Skip empty words
            if len(word) == 0:
                continue

        # Initialize a boolean array dp of size len(word) + 1 with all elements set to False
            dp = [False] * (len(word) + 1)
        # Set dp[0] to True, as an empty string is always a valid word
            dp[0] = True

        # Iterate through each index i in the range 0 to len(word)
            for i in range(len(word)):
        # If dp[i] is False, it means that the substring word[0:i] cannot be formed by
        #concatenating other words
        # So we can skip checking the substrings that start at this index
                if not dp[i]:
                    continue

        # Iterate through each index j in the range i+1 to len(word) + 1
                for j in range(i+1, len(word) + 1):
        # If j - i < len(word), it means that the substring word[i:j] is not the entire word
        # If substring word[i:j] is present in words_set, it means that this substring is a valid word
        # So we can mark dp[j] as True, as the substring word[0:j] can be formed by
        # concatenating valid words
                    if j - i < len(word) and word[i:j] in words_set:
                        dp[j] = True

        # If dp[-1] is True, it means that the word can be formed by concatenating other words from
        #  the input list
            if dp[-1]:
            
        # So we add it to the concatenated_words list
                concatenated_words.append(word)

    # Return the concatenated_words list
        return concatenated_words

# DFS with Memoization - O(NM^2)
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        @cache
        def dfs(word, count):
            if not word and count > 1:
                return True
            
            for i in range(len(word)):
                if word[:i+1] in dt and dfs(word[i+1:], count + 1):
                    return True
            
            return False
        
        dt = set(words)
        return [word for word in dt if dfs(word, 0)]


