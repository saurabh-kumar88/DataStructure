# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self, root):
      self.root = TreeNode(root)

    # def print_tree(self):
    #   return self.inorder_traverse( tree.root, " ")
    
    def inorder_traverse(self, node, k):
      
      if node == None:
        return False
      
      if(node.val == k):
        return True

      res1 = self.inorder_traverse(node.left, k)
      if res1:
        return True

      res2 = self.inorder_traverse( node.right, k)
      return res2 
            
      

    def kthSmallest(self, root: TreeNode, k: int) -> int:
      if self.inorder_traverse( root, k ):
        return k
      else:
        return False  


if __name__ == "__main__":
    tree = Solution(5)
    tree.root.left = TreeNode(3)
    tree.root.left.left = TreeNode(2)
    tree.root.left.left.right = TreeNode(None)
    tree.root.left.left.right = TreeNode(1)
    tree.root.left.right = TreeNode(4)
    tree.root.right = TreeNode(6)

    print( tree.kthSmallest(tree.root, 2) )
