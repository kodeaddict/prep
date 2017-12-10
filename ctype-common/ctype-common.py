
def listToInt(item):
   arr = (ctypes.c_int * len(item))(*item)
   return arr
