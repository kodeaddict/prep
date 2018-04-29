#!/usr/bin/python
import Tac
import sys
from DataTypes import TreeNode
from DataTypes import constructTree
import Util
import DataTypes

class SameTreeSolution(object):
   # https://leetcode.com/problems/same-tree/description/
   def isSameTree(self, p, q):
      if p and q:
         #print "   ", p.val, q.val
         return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
      #print "Checking if p is q: ", p, q
      return p is q

   def isSameTreeTuple(self, p, q):
      def t(n):
         if n:
            print "   ", n.val, n.left, n.right
         else:
            print "    n is None"
         val = n and (n.val, t(n.left), t(n.right))
         print "         val = ", val
         return val
      print "Check if equal p and q ", p.val, q.val
      r1val = t(p)
      r2val = t(q)
      print r1val, r2val
      return r1val == r2val

data = [3,5, "null", 2,1,4,6,7,8,9,10,11,12,13,14]
r1 = constructTree( data )
r2 = constructTree( data )
l = DataTypes.printTreeAsList( r1 )
print l, l == data

#Util.startFuncTracing( "isSameTree" )
same = SameTreeSolution().isSameTree( r1, r2 )
#Util.stopFuncTracing( " isSameTree" )
print "%s" % ( "same" if same else "not same" )
