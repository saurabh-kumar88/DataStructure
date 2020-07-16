class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        
        # print hierarchy of tree
        spaces = ' ' * self.get_level() * 5
        prefix = spaces + '| _ _' if self.parent else spaces
        print( prefix + self.data )
        
            
        # check if we reached to leafe nodes
        if self.children:
            for child in self.children:
                child.print_tree() # recursively calling print_tree() till reached to leaf nodes 

def product_tree():
    root = TreeNode("Electronics")

    
    laptops = TreeNode("Laptop")
    laptops.add_child(TreeNode('hp'))
    laptops.add_child(TreeNode('lenovo'))
    laptops.add_child(TreeNode('mac'))

    cellphones = TreeNode("Cell phone")
    cellphones.add_child(TreeNode('samsung galaxy'))
    cellphones.add_child(TreeNode('redmi'))
    cellphones.add_child(TreeNode('iphone'))

    tv = TreeNode("TV")
    tv.add_child(TreeNode('samsung'))
    tv.add_child(TreeNode('LG'))
    tv.add_child(TreeNode('Sony'))

    root.add_child(laptops)
    root.add_child(cellphones)
    root.add_child(tv)

    

    

    return root






if __name__ == "__main__":
    root = product_tree()
    root.print_tree()
    #print( root.get_level() )
    







