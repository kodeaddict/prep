#!/usr/bin/env python

from ctypes import *
import pdb

# TODO: Put this in base class
def listToInt(item):
   arr = (c_int * len(item))(*item)
   return arr

def hash_fn_py(a, b):
    print "hash_fn_py - ", a[0], b
    return a[0]/b

def cmp_fn_py(a, b):
    print "cmp_fn_py - ", a[0], b[0]
    if a[0] == b[0]:
        return 0;
    else:
        return -1;


HASHFUNC = CFUNCTYPE(c_ulong, POINTER(c_void_p), c_ulong)
CMPFUNC = CFUNCTYPE(c_int, POINTER(c_void_p), POINTER(c_void_p))

hash_fn = HASHFUNC(hash_fn_py)
cmp_fn = CMPFUNC(cmp_fn_py)


target = CDLL('../libtarget.so')

num = [1,2,3,4]
dupFound = target.check_duplicate_numbers(listToInt(num), len(num) )

# TODO add library for asserting and debugging
assert dupFound == False

print "Duplicate items present? %s" %( "YES" if dupFound else "NO")
