# _________________ Locations Tree hierarchy ___________________

class TreeNode:
    __LEVEL = 0
    def __init__(self, location_name):
        self.location_name = location_name
        self.children = []
        self.parent = None
        TreeNode.__LEVEL += 1

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
    
    def getLevel(self):
        return TreeNode.__LEVEL


    # print hierarchy of tree
    def print_tree(self, level):
        self.level = level
        
        spaces = ' ' * self.get_level() * 5
        prefix = spaces + '| _ _' if self.parent else ""
        if self.get_level() <= level :
            print( prefix + "{} ".format( self.location_name ) )
        else:
            pass
        

        if self.children:
            for child in self.children:
                child.print_tree(level)
                
                    
def build_locations_tree():
    
    # root node
    globe = TreeNode("Global")

    # India
    india = TreeNode("India")
    
    Gujrat = TreeNode("Gujrat")
    Gujrat.add_child(TreeNode("Ahmedabad"))
    Gujrat.add_child(TreeNode("Baroda"))
    
    Karnataka = TreeNode("Karnataka")
    Karnataka.add_child(TreeNode("Bagaluru"))
    Karnataka.add_child(TreeNode("Mysore"))
    
    india.add_child(Gujrat)
    india.add_child(Karnataka)

    # USA
    usa = TreeNode("USA")

    new_jersey = TreeNode("New Jersey")
    new_jersey.add_child(TreeNode("Priceton"))
    new_jersey.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain view"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(new_jersey)
    usa.add_child(california)

    # add to root node
    globe.add_child(india)
    globe.add_child(usa)

    return globe



def BST(val):







if __name__ == "__main__":
    root = build_locations_tree()
    # root.print_tree(3)

    BST(3)

    
    
   
    
    






