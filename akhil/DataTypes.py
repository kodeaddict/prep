
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None

def oldconstructTree( data ):
   #data = [3,5,2,1,4,6,7,8,9,10,11,12,13,14]
   n = iter(data)
   tree = TreeNode(next(n))
   fringe = deque([tree])
   while True:
      head = fringe.popleft()
      try:
         nxt = next(n)
         head.left = None if nxt == "null" else TreeNode(next(n))
         fringe.append(head.left)
         nxt = next(n)
         head.right = None if nxt == "null" else TreeNode(next(n))
         fringe.append(head.right)
      except StopIteration:
         break
   return tree

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

# print BreadthFirst
def printTreeAsList( root ):
   stack = [root]
   nodes = []
   index = 0
   while stack:
      cur_node = stack[0]
      stack = stack[1:]
      index += 1
      if cur_node == "null":
         nodes.append( cur_node )
      else:
         nodes.append( cur_node.val )
         lastNonNullIndex = index
         # left node
         item = "null" if cur_node.left == None else cur_node.left
         stack.append( item )
         # right node
         item = "null" if cur_node.right == None else cur_node.right
         stack.append( item )

   return nodes[:lastNonNullIndex]
