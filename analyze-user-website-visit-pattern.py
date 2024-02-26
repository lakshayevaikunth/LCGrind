# Trie Approach
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

def insert(trie, sequence):
    node = trie
    for site in sequence:
        if site not in node.children:
            node.children[site] = TrieNode()
        node = node.children[site]
    node.count += 1

def dfs(node, path, result):
    if node.count > result[1]:
        result[0] = path
        result[1] = node.count
    for child in node.children:
        dfs(node.children[child], path + [child], result)

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Combine the lists into a list of tuples and sort by timestamp
        webInfo = sorted(zip(timestamp, username, website))

        # Construct a dictionary where keys are usernames and values are lists of visited websites
        userWebsites = {}
        for _, user, site in webInfo:
            userWebsites.setdefault(user, []).append(site)

        # Construct a trie to store website sequences and their counts
        trie = TrieNode()
        for sites in userWebsites.values():
            visited = set()  # Keep track of unique sequences for each user
            n = len(sites)
            for i in range(n - 2):  # Slide a window of size 3 over the list of websites
                for j in range(i + 1, n - 1):
                    for k in range(j + 1, n):
                        sequence = (sites[i], sites[j], sites[k])
                        if sequence not in visited:
                            insert(trie, sequence)
                            visited.add(sequence)

        # Find the most visited sequence
        result = [None, 0]
        dfs(trie, [], result)

        # Return the most visited sequence
        return result[0]


# Sliding Window Approach

from collections import defaultdict

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Combine the lists into a list of tuples and sort by timestamp
        webInfo = sorted(zip(timestamp, username, website))

        # Construct a dictionary where keys are usernames and values are lists of visited websites
        userWebsites = defaultdict(list)
        for _, user, site in webInfo:
            userWebsites[user].append(site)

        # Construct a dictionary to count the occurrence of website sequences
        sequenceCount = defaultdict(int)
        for sites in userWebsites.values():
            visited = set()  # Keep track of unique sequences for each user
            n = len(sites)
            for i in range(n - 2):  # Slide a window of size 3 over the list of websites
                for j in range(i + 1, n - 1):
                    for k in range(j + 1, n):
                        sequence = (sites[i], sites[j], sites[k])
                        if sequence not in visited:
                            sequenceCount[sequence] += 1
                            visited.add(sequence)

        # Find the most visited sequence(s)
        maxCount = max(sequenceCount.values())
        mostVisited = [seq for seq, count in sequenceCount.items() if count == maxCount]

        # Return the lexicographically smallest sequence
        return min(mostVisited)


