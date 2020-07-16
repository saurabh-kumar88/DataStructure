# _________________ Employees Tree hierarchy ___________________

class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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

    # print hierarchy of tree
    def print_tree(self, option=None):
        self.option = option

        spaces = ' ' * self.get_level() * 5
        prefix = spaces + '| _ _' if self.parent else spaces
             

        if option != None and option.lower() == "name":
            print( prefix + "{}".format( self.name ) )
        elif option != None and option.lower() == "designation":
            print( prefix + "{}".format( self.designation ) )
        else:
            print( prefix + "{}  ( {} ) ".format( self.name ,self.designation ) )
        
        # check if we reached to leafe nodes
        if self.children:
            for child in self.children:
                child.print_tree(option) # recursively calling print_tree() till reached to leaf nodes

    
def employees_tree():
    
    # CEO (root node)
    ceo = TreeNode("Nilupul", "CEO")

    # CTO
    cto = TreeNode("Chinmay", "CTO")

    # Infra head
    infra_head = TreeNode("Vishwa", "Infrastructure head")
    infra_head.add_child(TreeNode("Dhaval", "Cloud manager"))
    infra_head.add_child(TreeNode("Dhaval", "Python developer"))
    infra_head.add_child(TreeNode("Abhijit", "App manager"))
    
    # Application head
    application_head = TreeNode("Aamir", "Application head")
    
    cto.add_child(infra_head)
    cto.add_child(application_head)

    # HR Head
    gels = TreeNode("Gels", "HR Head")
    gels.add_child(TreeNode("Peter", "Recruitment manager"))
    gels.add_child(TreeNode("Waqas", "Policy manageger"))

    ceo.add_child(cto)
    ceo.add_child(gels)

    return ceo



if __name__ == "__main__":
    root = employees_tree()
    root.print_tree("")
   
    #print( root.get_level() )
    
    






