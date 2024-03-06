# Regular Expression
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # brute force solution use builtin re lib to do heavy lifting
        # edge case bad regex pattern passed in
        while '**' in p:
            p = p.replace('**', '*')
        regex = '^' + p + '$'
        return re.search(regex, s)

import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        while "**" in p:
            p = p.replace("**","*")

        res = re.findall(p,s)
        if len(res)==0:
            return False
        
        res = res[0]
        return s==res

# Brute Force - Recursive backtracking approach
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Define a recursive function to check if the substring of s matches the pattern p
        def match(i, j):
            # If both strings are empty, they match
            if i == len(s) and j == len(p):
                return True
            # If pattern is empty but string is not, they don't match
            if j == len(p):
                return False
            # If string is empty but pattern has remaining characters, check for '*'
            if i == len(s):
                # If the current pattern character is followed by '*', check for the next character
                if j + 1 < len(p) and p[j + 1] == '*':
                    return match(i, j + 2)
                # Otherwise, they don't match
                else:
                    return False
            # If the current characters match or pattern character is '.', move to the next characters
            if s[i] == p[j] or p[j] == '.':
                # If the next pattern character is '*', explore both possibilities
                if j + 1 < len(p) and p[j + 1] == '*':
                    return match(i + 1, j) or match(i, j + 2)
                # Otherwise, move to the next characters in both strings
                else:
                    return match(i + 1, j + 1)
            # If the current characters don't match and the next pattern character is '*', skip it
            elif j + 1 < len(p) and p[j + 1] == '*':
                return match(i, j + 2)
            # Otherwise, they don't match
            else:
                return False
        
        # Start the recursive matching process from the beginning of both strings
        return match(0, 0)

# Bottom Up Apporach - Tabulation

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Initialize a 2D array `memory` with dimensions (len(s) + 1) x (len(p) + 1)
        memory = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        # Set memory[len(s)][len(p)] to True since an empty substring of s and an empty pattern p match
        memory[len(s)][len(p)] = True

        # Iterate through the substrings of s and patterns p from the end towards the beginning
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                # Check if the current characters match or if the pattern character is '.'
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")

                if (j + 1) < len(p) and p[j + 1] == "*":
                    # If the next character in the pattern is '*', handle the '*' wildcard character
                    memory[i][j] = memory[i][j + 2]
                    if match:
                        memory[i][j] = memory[i + 1][j] or memory[i][j]
                elif match:
                    # If the characters match, move to the next characters in both strings
                    memory[i][j] = memory[i + 1][j + 1]

        # Return memory[0][0], which represents whether the entire s matches the entire p
        return memory[0][0]

  
