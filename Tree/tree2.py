from collections import deque

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def depth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return max(left_depth, right_depth) + 1


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_search(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_search(tree.root, "")
        elif traversal_type=="postorder":
            return self.postorder_print(tree.root, "")
        else:
            print("This Traversal type : `{}` is not supported ".format(traversal_type) ) 
            return False

    def preorder_search(self, start, traversal):
        """Root --> Left->right->left.left->left.right"""    

        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_search(start.left, traversal)
            traversal = self.preorder_search(start.right, traversal)
        return traversal

    def inorder_search(self, start, traversal_type ):
        """Search left sub tree nodes first : Left --> Root --> Right"""
        traversal = ""
        if start:
            traversal = self.preorder_search(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.preorder_search(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
    
    # preorder search
    def traverse(self, start):
        traversal = ""
        if start:
            traversal += str(start.value) 
            traversal = self.traverse(start.left.value)
            traversal = self.traverse(start.right.value)
        return traversal



    
class Solution(object):
    def isCousins(self, root, x: int, y: int) -> bool:    
        
        if self.get_level(root, x ) == self.get_level(root, y ):
            if self.parent_search(root, x) != self.parent_search(root, y):
                return True
        return False

    def get_level(self, root, node_value):
        Q = []
        level = 1

        Q.append(root)
        Q.append(None)
        while(len(Q)):
            temp = Q[0]
            Q.pop(0)
            if( temp == None ):
                if len(Q) == 0:
                    return None
                if (Q[0] != None):
                    Q.append(None)
                level += 1
            
            else:
                if( temp.value == node_value ):
                    return level
                if (temp.left):
                    Q.append(temp.left)
                if (temp.right):
                    Q.append(temp.right)
        return 0

    def parent_search(self, root, child_node):
        if not root: 
            return None
        if root.left and root.left.value == child_node:
             return root
        if root.right and root.right.value == child_node: 
            return root
        return self.parent_search(root.left, child_node) or self.parent_search(root.right, child_node) 
    

            




            

#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7 





if __name__ == "__main__":
    # initialize tree

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    # tree.root.right.left = Node(6)
    # tree.root.right.right = Node(7)

    print( tree.print_tree("preorder") )
    # print( tree.print_tree("inorder") )
    # print( tree.print_tree("postorder") )

    # obj = Solution()
    # result = obj.isCousins( tree.root, 4, 7 )
    # print(result)



    