# Naive

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Check if the length of the string is less than 2
        if len(s) < 2:
            return len(s)
        
        # Initialize variables
        k, max_len, count = 0, 0, 0
        
        # Iterate through the string
        for i in range(1, len(s)):
            # Check for repeating characters in the current substring
            for j in range(k, i):
                if s[i] == s[j]:
                    k = j + 1
            
            # Update the current substring length
            count = i - k + 1
            
            # Update the maximum length
            if count > max_len:
                max_len = count
        
        # Return the result
        return max_len

# Sliding window technique

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = 0
        length = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                length = max(length, r - l + 1)
            seen[char] = r

        return length

# Two Pointer

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        if not s:
            return 0
        if len(set(s))==1:
            return 1
        counter , begin, end, len_ = defaultdict(int), 0, 0, 0
        while end < len(s):
            # Checking that no char is repeated
            # if not repeated then record the lengbth of teh current substring if it is the longest till now
            # move the end pointer forward to keep checking if a longer substring exists.
            counter[s[end]] +=1
            if all([n<=1 for n in counter.values()]):
                curr_len = len(s[begin:end+1])
                len_ = curr_len if len_ < curr_len else len_

            # if the chars are not unique then move the begin pointer until the substring is made up of unique chars again.
            while any([n>1 for n in counter.values()]):
                counter[s[begin]] -=1
                begin +=1    
            end+=1
        return len_
        
