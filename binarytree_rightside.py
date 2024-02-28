# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, depth):
            if node:
                if depth == len(ans):
                    ans.append(node.val)
                dfs(node.right, depth+1)
                dfs(node.left, depth+1)
        ans = []
        dfs(root, 0)
        return ans

# BFS with queue

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []  # Initialize an empty list to store the rightmost values
        q = collections.deque([root])  # Initialize a deque with the root node
        
        # Perform BFS traversal
        while q:
            rightMost = None  # Initialize a variable to track the rightmost node at each level
            n = len(q)  # Get the number of nodes at the current level
            
            # Iterate through each node at the current level
            for i in range(n):
                node = q.popleft()  # Dequeue a node from the left of the deque
                if node:
                    rightMost = node  # Update the rightmost node
                    q.append(node.left)  # Enqueue the left child
                    q.append(node.right)  # Enqueue the right child
            
            # If a rightmost node was encountered at the current level, append its value to the result
            if rightMost:
                result.append(rightMost.val)
        
        return result  # Return the list containing the rightmost values





        
