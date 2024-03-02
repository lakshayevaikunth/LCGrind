# Brute force
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        q = []
        n = len(graph)
        for i in range(n):
            visit = set()
            visit.add(i)
            q.append([i, visit])
        
        steps = 0
        while q:
            num = len(q)
            for i in range(num):
                node, visit = q.pop(0)
                #print(node, visit)
                if len(visit) == n:
                    return steps
                for nei in graph[node]:
                    temp = visit.copy()
                    temp.add(nei)
                    q.append([nei, temp])
            if q:steps += 1

# BFS with Bit manupulation

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        target = (1 << n) - 1  # Bitmask representing all nodes visited

        # Initialize the queue with tuples (node, bitmask)
        q = collections.deque([(i, 1 << i) for i in range(n)])

        # Use a set to track visited states
        visited = set((i, 1 << i) for i in range(n))

        steps = 0
        while q:
            size = len(q)
            for _ in range(size):
                node, bitmask = q.popleft()
                if bitmask == target:
                    return steps
                for nei in graph[node]:
                    new_bitmask = bitmask | (1 << nei)
                    if (nei, new_bitmask) not in visited:
                        q.append((nei, new_bitmask))
                        visited.add((nei, new_bitmask))
            steps += 1

        return -1  # No solution found




