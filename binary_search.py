#! /home/kamraa/anaconda3/bin/python3 -tt

# Node class
# Class Variables - 
# Attributes - left_node, right_node, data (int)
# Methods - constructor, destructor
class node:
  # Class Variables
  init_val = 0

  # init 1
  def __init__(self, data):
    self.data = data
    self.left_node = None
    self.right_node = None

# Tree class
# Class Variables - 
# Attributes - top_node, num_nodes
# Methods - insert(), delete(), find(), print()
class BinaryTree:

  # init
  def __init__(self, data):
    self.top_node = node(data)
    self.num_nodes = 1

  # init
  def __init__(self):
    self.top_node = None
    self.num_nodes = 0

  # insert a new node
  # Return: 0 - Success, anything else - Failure
  def insert(self, in_node):

    node = self.top_node

    # first node - easy
    if node is None:
      self.top_node = in_node
      #print("Node inserted "+str(in_node.data))
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
          self.num_nodes += 1
          #print("Node inserted "+str(in_node.data))
          return 0
        else:                              # go one
          node = node.left_node
          continue;

      # go right
      if in_node.data > node.data:
        if node.right_node is None:       # found the place to insert
          node.right_node = in_node
          self.num_nodes += 1
          #print("Node inserted "+str(in_node.data))
          return 0
        else:                             # go one
          node = node.right_node
          continue;      
    
  # delete a node
  # Return: 0 - Success, anything else - Failure
  def delete(self, node):
    pass
  # search for a node
  # Return: node if found, a negative number otherwise
  def find(self, node):
    pass

  # print the entire tree structure
  # order - pre-order, post order, in-order
  # Return: 0 - Success, anything else - Failure
  def print(self, order):

    if order == 'in':  
      node = self.top_node

      if node is None:
        print("Empty Tree. Nothing to print")
        return -1

      stack = []
      from_stack = False
      while True:

        if from_stack and node.right_node is not None:
          print(node)
          stack.pop()
          if len(stack) != 0:
            node = stack[len(stack) -1]
            from_stack = True
            continue;                    
          else:
            # if not from stack or has a right node put the nodes on the stack
            if node.right_node is not None:
              stack.append(node.right_node)      
            if not from_stack:
              stack.append(node)        

        if node.left_node is not None:
          node = node.left_node
          from_stack = False
          continue;
        else:
          print(node)
          stack.pop()
          if len(stack) != 0:
            node = stack[len(stack) -1]
            from_stack = True
            continue;                    
          else:
            return 0

def main():

  # read data from a file called numbers.dat
  try:
    f = open("numbers.dat","r")
  except(IOError):
    print("file does not exist")
    return -1
  
  # create an empty tree to begin with
  tree = BinaryTree()

  # create a binary tree by adding nodes as you read the numbers
  print("printing the numbers as they are being read")
  for num in f:
    print(num,)
    n = node(num)
    tree.insert(n)
    
  # print the tree
  print("printing the tree")
  tree.print("in")

if __name__ == '__main__':
  main()



