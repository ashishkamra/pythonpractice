#! $HOME/anaconda3/bin/python3 -tt

import random

# Node class
# Class Variables - 
# Attributes - left_node, right_node, data (int)
# Methods - constructor, destructor
class a_node:
  # Class Variables
  init_val = 0

  # init 1
  def __init__(self, data):
    self.data = data
    self.left_node = None
    self.right_node = None
    self.parent_node = None

# Tree class
# Class Variables - 
# Attributes - top_node, num_nodes
# Methods - insert(), delete(), find(), print()
class BinaryTree:

  # init
  def __init__(self, data):
    self.top_node = a_node(data)
    self.num_nodes = 1
    self.left_height = 1
    self.right_height = 1

  # init
  def __init__(self):
    self.top_node = None
    self.num_nodes = 0
    self.height = 0

  # in-oder printing - sorted
  def process_in(self, node):
    if node.left_node is not None:
      self.process_in(node.left_node)

    print(node.data)

    if node.right_node is not None:
      self.process_in(node.right_node)
  
  #pre-order printing
  def process_pre(self, node):
    print(node.data)

    if node.left_node is not None:
      self.process_pre(node.left_node)

    if node.right_node is not None:
      self.process_pre(node.right_node)

  # post-order printing
  def process_post(self, node):
    
    if node.left_node is not None:
      self.process_post(node.left_node)

    if node.right_node is not None:
      self.process_post(node.right_node)

    print(node.data)

  # insert a new node
  # Return: 0 - Success, anything else - Failure
  def insert(self, in_node):

    node = self.top_node
    height = 0

    # case 1 - first node
    if node is None:
      self.top_node = in_node
      #print("Top node inserted "+str(in_node.data))
      self.num_nodes += 1
      height += 1
      self.left_height = height
      self.right_height = height
      return 0    

    # traverse from top_node to find the right location to insert the node
    while True:
      if in_node.data == node.data:
        print("Node already exists")
        return -1
      
      #go left
      if in_node.data < node.data:
        if node.left_node is None:         # found the place to insert
          node.left_node = in_node
          node.left_node.parent_node = node
          self.num_nodes += 1
          #print("Node inserted to left "+str(in_node.data))
          if height > self.left_height:
            self.left_height = height
          return 0
        else:                              # go on
          node = node.left_node
          height += 1
          continue;

      # go right
      if in_node.data > node.data:
        if node.right_node is None:       # found the place to insert
          node.right_node = in_node
          node.right_node.parent_node = node
          self.num_nodes += 1
          #print("Node inserted to right "+str(in_node.data))
          if height > self.right_height:
            self.right_height = height
          return 0
        else:                             # go on
          node = node.right_node
          height += 1
          continue;      

  # Merge left subtree to right subtree
  def _merge_right(self, left_subtree, right_subtree):
    #just go to the left most node of the right subtree and insert there
    tmp_node = None
    if right_subtree.left_node is not None:
      tmp_node = right_subtree.left_node
      while tmp_node.left_node is not None and tmp_node.right_node is not None:
        tmp_node = tmp_node.left_node
    else:
      tmp_node = right_subtree
    
    tmp_node.left_node = left_subtree
    left_subtree.parent_node = tmp_node
   
  # delete a node
  # Return: 0 - Success, anything else - Failure
  def delete(self, data):
    
    # find the node to delete
    node = self.find(data)

    if node is not None:  # found the node

      # diagonistics
      print("node = "+str(node.data))
      if node.parent_node is not None:
        print("parent node = "+str(node.parent_node.data))
      if node.left_node is not None:
        print("left node = "+str(node.left_node.data))
      if node.right_node is not None:
        print("right node = "+str(node.right_node.data))
     
      # case 1 edge case - the only node in the tree
      if node.left_node is None and node.right_node is None and node.parent_node is None:
        self.top_node = None
        print("deleted at case 1")

      # case 2 leaf node
      if node.parent_node is not None and node.left_node is None and node.right_node is None:
        if node.parent_node.left_node == node:
          node.parent_node.left_node = None
        if node.parent_node.right_node == node:
          node.parent_node.right_node = None
        print("deleted at case 2")

      # case 3 middle node - no right subtree
      if node.parent_node is not None and node.right_node is None and node.left_node is not None:
        if node.parent_node.left_node == node:
          node.parent_node.left_node == node.left_node
        elif node.parent_node.right_node == node:
          node.parent_node.right_node == node.left_node
        print("deleted at case 3")

      # case 4 middle node - no left subtree
      if node.parent_node is not None and node.left_node is None and node.right_node is not None:
        if node.parent_node.left_node == node:
          node.parent_node.right_node == node.right_node
        elif node.parent_node.right_node == node:
          node.parent_node.right_node == node.left_node

        print("deleted at case 4")

      # case 5 both subtrees - need to merge
      if node.left_node is not None and node.right_node is not None:

        # merge right always - we can merge left as well depending on which on leads to a more balanced tree
        self._merge_right(node.left_node, node.right_node)      

        if node.parent_node is not None:              # adjust the right node to parent node
          if node.parent_node.left_node == node:
            node.parent_node.left_node = node.right_node
          elif node.parent_node.right_node == node:
            node.parent_node.right_node = node.right_node
        else:                                         # make the right node the top node
          self.top_node = node.right_node
      
        print("deleted at case 5")

      del node
      self.num_nodes -= 1
      return 0

    else:                 # did not find the node
      return -1


  # internal function for recursion
  def find_in(self, data, node):

    #print("checked "+str(node.data))

    ret_val = None

    if node.data == data:     #found
      return node
    elif node.left_node is None and node.right_node is None: #not found
      return None

    #go left
    if node.left_node is not None and data < node.data:
      ret_val = self.find_in(data, node.left_node)
      if ret_val is not None:
        return ret_val

    #go right
    if node.right_node is not None and data > node.data:
      ret_val = self.find_in(data, node.right_node)  
      if ret_val is not None:
        return ret_val

    return ret_val

  # search for a node
  # Return: node if found, None otherwise
  def find(self, data):

    # start at top
    node = self.top_node
    return self.find_in(data, node) 

  # print the entire tree structure
  # order - pre-order, post order, in-order
  # Return: 0 - Success, anything else - Failure
  def print(self, order):

    node = self.top_node

    if node is None:
      print("Empty Tree. Nothing to print")
      return -1

    if order == 'in':  
      self.process_in(node)
      return 0
    elif order == 'pre':
      self.process_pre(node)
      return 0
    elif order == 'post':
      self.process_post(node)   
      return 0
    else:
      print("Incorrect option")
      return -1

def main():

  # read data from a file called numbers.dat
  try:
    f = open("numbers.dat","r")
  except(IOError):
    print("file does not exist")
    return -1
  
  # create an empty tree
  tree = BinaryTree()

  # list comprehension to read the numbers in a list
  num_list = [num for num in f]
  
  # randomize to get balanced tree
  # random.shuffle(num_list)

  # insert numbers one by one
  for num in num_list:
    tree.insert(a_node(int(num)))
    
  # print the tree and vital stats
  print("tree height = "+str(max(tree.left_height, tree.right_height)))
  print("tree nodes = "+str(tree.num_nodes))
  print("In-order printing the tree")
  tree.print("in")

  #print("pre-order printing the tree")
  #tree.print("pre")
  
  #print("post-order printing the tree")
  #tree.print("post")

  #num_find = 76
  #if tree.find(int(num_find)) is not None:
  #  print("found "+str(num_find))
  #else:
  #  print("not found "+str(num_find))

  num_delete = 5
  if tree.delete(int(num_delete)) == 0:
    print("deleted "+str(num_delete))
  else:
    print("did not find the number "+str(num_delete))

  # print the tree and vital stats
  print("tree height = "+str(max(tree.left_height, tree.right_height)))
  print("tree nodes = "+str(tree.num_nodes))
  print("In-order printing the tree")
  tree.print("in")


if __name__ == '__main__':
  main()



