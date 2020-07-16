class Node:
    def __init__(self, relation, name):
        self.relation = relation
        self.name = name
        self.right = None
        self.left = None


class Family_tree:

    

    def __init__(self, relation):
        self.relation = relation
        self.right = None
        self.left = None
        

    "Helper method to choose traversal algorithm"
    def _traverse_tree(self,  traversing_algorithm):
        if traversing_algorithm.lower() == "preorder":
            return self.preorder_traversal(root, "")

    def preorder_traversal(self, start, traverse):
        "root --> left --> right"
        if start:
            traverse +=  " {} --> ".format( start.relation ) 
            traverse = self.preorder_traversal(start.left, traverse )
            traverse = self.preorder_traversal(start.right, traverse )
        return traverse



if __name__ == "__main__":
    root = Family_tree('Grand father')
    root.left = Family_tree("Son")
    root.right = Family_tree("Daughter")

    root.left.right = Family_tree("Grand son")
    root.left.left = Family_tree("Grand daughter")
    


    # root.left.left = Family_tree("Grand Son", "Ronnie")
    # root.left.right = Family_tree("Grand Daughter", "Maria")

    
    # root.right.left = Family_tree("Grand Daughter", "kindel")
    # root.right.right = Family_tree("Grand son", "Jimmy")

    print( root._traverse_tree("preOrder") )
    




