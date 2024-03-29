# BFS

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create a prerequisite dict. (containing courses (nodes) that need to be taken (visited)
		# before we can visit the key.
        preq = {i:set() for i in range(numCourses)}
		# Create a graph for adjacency and traversing.
        graph = collections.defaultdict(set)
        for i,j in prerequisites:
		    # Preqs store requirments as their given.
            preq[i].add(j)
			# Graph stores nodes and neighbors.
            graph[j].add(i)
        
        q = collections.deque([])
		# We need to find a starting location, aka courses that have no prereqs.
        for k, v in preq.items():
            if len(v) == 0:
                q.append(k)
		# Keep track of which courses have been taken.
        taken = []
        while q:
            course = q.popleft()
            taken.append(course)
			# If we have visited the numCourses we're done.
            if len(taken) == numCourses:
                return taken
			# For neighboring courses.
            for cor in graph[course]:
			    # If the course we've just taken was a prereq for the next course, remove it from its prereqs.
                preq[cor].remove(course)
				# If we've taken all of the preqs for the new course, we'll visit it.
                if not preq[cor]:
                    q.append(cor)
		# If we didn't hit numCourses in our search we know we can't take all of the courses.
        return []

# Topological sort - Kahn's algorithm

from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Build the graph
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # Step 2: Calculate the in-degree of each node
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            in_degree[course] += 1
        
        # Step 3: Perform topological sort
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Check for cycle
        if len(result) < numCourses:
            return []
        
        return result
