# DFS with Recursion and Incremental Counting
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        nums = defaultdict(int)

        def dfs(node, odd):
            if not node: return 0
            nums[node.val] += 1
            nextOdd = odd + (1 if nums[node.val] % 2 else -1)
          
            if not node.left and not node.right:
                nums[node.val] -=1
                return nextOdd <= 1
                
            left = dfs(node.left, nextOdd)
            right = dfs(node.right, nextOdd)
            nums[node.val] -= 1
            return left + right 
        return +dfs(root, 0)
        

# Brute Force DFS

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        if not root: return 0 # Base case
        cnt = 0 # number of pseudo-palindromic paths
        count = defaultdict(int) # for storing the number of occurences

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal cnt, count
            count[node.val] += 1 # increase the count

            # if we reach the leaf node, check for pseudo-palindromic array
            if not node.left and not node.right:
                odds = 0 # count number of odd occurences
                for key in count:
                    if count[key] % 2:
                        odds += 1
                        if odds > 1: break
                if odds <= 1: cnt += 1 # if it follows all requirements, then we found an answer!
            
            # traverse both subtrees
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
            count[node.val] -= 1 # reduce the count, since we are moving backwards to find other paths
        
        dfs(root)
        return cnt
