# DFS
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # Prepare a visited array
        visitedArray = [[0 for _ in range(cols)] for _ in range(rows)]

        # Write inline function
        def visitIsland(row, col):
            # Check boundary conditions + node should not be 0 + node should not be visited already
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == "0" or visitedArray[row][col]:
                return
            
            # Mark the node as visited
            visitedArray[row][col] = 1

            # Traverse in all four direction recursively.
            visitIsland(row, col + 1)
            visitIsland(row, col - 1)
            visitIsland(row + 1, col)
            visitIsland(row - 1, col)

        count = 0
        for row in range(rows):
            for col in range(cols):
                if not visitedArray[row][col] and grid[row][col] == "1":
                    # Do DFS traversal and increase the count
                    visitIsland(row, col)
                    count += 1
        return count


# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check if the grid is empty
        if not grid or not grid[0]:
            return 0

        islands = 0  # Initialize the count of islands
        visit = set()  # Set to keep track of visited cells
        rows, cols = len(grid), len(grid[0])  # Get the number of rows and columns

        # Define a depth-first search (DFS) function
        def dfs(r, c):
            # Check for out-of-bounds, water, or already visited cells
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))  # Mark the current cell as visited
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # Possible directions (up, down, left, right)
            
            # Explore neighbors using DFS
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell contains land and has not been visited
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1  # Increment the island count
                    dfs(r, c)  # Explore the island using DFS

        return islands  # Return the total number of islands
