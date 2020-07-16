class Binary_search_tree:
  
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def add_child(self, data):
    if data == self.data:
      return

    if data < self.data:
      # add to left
      if self.left:
        self.left.add_child(data)
      else:
        self.left = Binary_search_tree(data)
    
    else:
      # add to right
      if self.right:
        self.right.add_child(data)
      else:
        self.right = Binary_search_tree(data)

  
  def inorder_traversal(self):
    "left-->node-->right"
    elements = []
    
    # visit left subtree
    if self.left:
      elements += self.left.inorder_traversal()
      
    # visit base node
    elements.append(self.data)
    
    # visit right subtree
    if self.right:
      elements += self.right.inorder_traversal()
      
    return elements
  
  def post_order_traversal(self, elements):
    "left-->right-->node"
   
    # visit left subtree
    if self.left:
      elements = self.left.post_order_traversal(elements)
      
    # visit right subtree
    if self.right:
      elements = self.right.post_order_traversal(elements)

    # visit base node
    elements.append(self.data)
    
    return elements
  
  def pre_order_traversal(self, elements):
    "node-->left-->right"
     
    # visit node
    elements.append(self.data)  

    # visit left subtree

    if self.left:
      elements = self.left.pre_order_traversal(elements)

    # visit right subtree
    if self.right:
      elements = self.right.pre_order_traversal(elements)

    
    return elements


  def search(self, val):

    if self.data is None or self.data == val: 
      return True
    
    else:  
      if val < self.data:
        if self.left:
          return self.left.search(val)
        else:
          return False
      
      if val > self.data:
        if self.right:
          return self.right.search(val)
        else:
          return False
  
  # def delete(self, val):

  #   # base case
    
  #   # binary search
  #   if val < self.data:
  #     if self.left:
  #       self.left = self.left.delete(val)
    
  #   elif val > self.data:
  #     if self.right:
  #       self.right = self.right.delete(val)
    
  #   # if val is same as root i.e val == self.data 
  #   # it means the val to be deleted is root

  #   else:
  #     if (self.left is None) and (self.right is None):
  #       return None
        
  #     # case1: Node with only one child or no child(leaf node)
  #     elif self.left is None:
  #       return self.right
      
  #     elif self.right is None:
  #       return self.right
      
  #     # case2: Node with two children--> get the inorder successor 
  #     # i.e smallest in the right subtree

  #     min_val = self.right.find_min()
  #     # copy the inorder successor to this temp node
  #     self.data = min_val
      
  #     # delete the inorder successor
  #     self.right = self.right.delete(min_val)

  #   return self

  def delete(self, val):
    if val < self.data:
      if self.left:
        self.left = self.left.delete(val)
    elif val > self.data:
      if self.right:
        self.right = self.right.delete(val)
    else:
      if self.left is None and self.right is None:
        return None
      elif self.left is None:
        return self.right
      elif self.right is None:
        return self.right

      min_val = self.right.find_min()
      self.data = min_val
      self.right = self.right.delete(min_val)

    return self
  
  def find_min(self):
    
    if self.left is None:
      return self.data
    return self.left.find_min()
  
  def find_max(self):

    if self.right is None:
      return self.data
    return self.right.find_max()

  def Sum(self):
    arr = self.inorder_traversal()
    return sum(arr)


# helper method
def build_tree(elements):
  root = Binary_search_tree(elements[0])
  for i in range(1,len(elements)):
    root.add_child(elements[i])
  
  return root


numbers = [20, 30, 40, 50, 60, 70, 80]


# _____________ Exercise ______________
# 1. find_min(): finds minimum element in entire binary tree
# 2. find_max(): finds maximum element in entire binary tree
# 3. calculate_sum(): calculates sum of all elements
# 4. post_order_traversal(): performs post order traversal of a binary tree
# 5. pre_order_traversal(): performs pre order traversal of a binary tree


if __name__ == "__main__":
  
  root = build_tree(numbers)
  
  # print("inorder traversal : ", root.inorder_traversal())
  # print("pre order traversal : ", root.pre_order_traversal([]))
  # print("post order traversal : ",root.post_order_traversal([]))

  # print(root.find_min())
  # print( root.find_max() )
  # print( root.Sum() )
  
  
  print(root.inorder_traversal())
  # root.delete(30)
  root.delete(20)
  print(root.inorder_traversal())
  

  




    
    




    