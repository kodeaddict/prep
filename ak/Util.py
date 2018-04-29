
import sys
import inspect
import DataTypes

traceFunctions = set()

def tracefunc(frame, event, arg, indent=[0]):
   def getArguments( fr ):
      args = inspect.getargvalues( fr )
      passed = []
      for arg in args.args:
         if arg == 'self':
            passed.append( 'self' )
            continue
         val = args.locals[ arg ]
         if isinstance( val, DataTypes.TreeNode ):
            passed.append( arg + ":" + str( val.val ) )
         else:
            passed.append( arg + ":" + str( val ) )
      return passed

   if 'None' in traceFunctions or frame.f_code.co_name in traceFunctions:
      if event == "call":
         args = getArguments( frame )
         indent[0] += 2
         print "-" * indent[0] + "call function", frame.f_code.co_name, "args: ", args
      elif event == "return":
         print "-" * indent[0] + "exit function", frame.f_code.co_name, "return: ", arg
         indent[0] -= 2
   return tracefunc

def startFuncTracing( name='None' ):
   traceFunctions.add( name )
   sys.setprofile( tracefunc ) 

def stopFuncTracing( name='None' ):
   assert name in traceFunctions
   traceFunctions.remove( name )
   sys.setprofile( None )
   
