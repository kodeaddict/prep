
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None

# data is read as level order list. "null" indicates no child
def constructTree( data ):
   assert data[0] != "null"
   root = None
   root = TreeNode( data[0] )
   parents = deque() # just a queue for FIFO
   parents.append( root )
   index = 0
   while True:
      assert parents, "There can not be no parents"
      pnode = parents.popleft()
      def makeChild():
         item = data[index]
         node = None if item == "null" else TreeNode( item ) 
         if node:
            parents.append( node )
         return node
      index += 1
      if index == len(data):
         break
      lnode = makeChild()
      index += 1
      if index == len(data):
         break
      rnode = makeChild()
      pnode.left = lnode
      pnode.right = rnode
   return root

# print BreadthFirst (level order)
def printTreeAsList( root ):
   queue = deque() # FIFO
   queue.append( root )
   nodes = []
   index = 0
   while queue:
      cur_node = queue.popleft()
      index += 1
      if cur_node == "null":
         nodes.append( cur_node )
      else:
         nodes.append( cur_node.val )
         lastNonNullIndex = index
         # left node
         item = "null" if cur_node.left == None else cur_node.left
         queue.append( item )
         # right node
         item = "null" if cur_node.right == None else cur_node.right
         queue.append( item )

   return nodes[:lastNonNullIndex]
