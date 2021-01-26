
from .classifier import classify
from .instances import HARD
from .problem import Problem, Type
import sys, getopt

def usage():
  print('classifier.py -n {<node constraint 1>, <node constraint 2>, ...} -e {<edge constraint 1>, ...}')

def checkFormalismForTrees(settingType):
  if settingType == Type.TREE:
    print("Do not specify any constraints other than edge-constr when --type option is 'tree'")
    sys.exit(1)

def parseConstraints(constrArg):
  return set([x.strip() for x in constrArg.strip()[1:-1].split(',') if x.strip() != ''])

def parseType(arg):
  if arg in ("directed", "dir"):
    return Type.DIRECTED
  elif arg in ("undirected", "undir"):
    return Type.UNDIRECTED
  elif arg in ("tree"):
    return Type.TREE
  else:
    print("Unhandled type specified: " + arg)
    sys.exit(1)

def main():
  try:
    opts, args = getopt.getopt(
      sys.argv[1:],
      "ht:n:e:",
      [
        "help",
        "type=",
        "node-constr=",
        "edge-constr=",
        "start-constr=",
        "end-constr="
      ])
  except getopt.GetoptError as err:
    print(err)
    usage()
    sys.exit(2)

  nodeConstr = {}
  edgeConstr = {}
  startConstr = {}
  endConstr = {}
  settingType = ""

  for opt, arg in opts:
    if opt in ("-h", "--help"):
      usage()
      sys.exit()
    elif opt in ("-t", "--type"):
      settingType = parseType(arg)
    elif opt in ("-n", "--node-constr"):
      checkFormalismForTrees(settingType)  
      nodeConstr = parseConstraints(arg)
    elif opt in ("-e", "--edge-constr"):
      edgeConstr = parseConstraints(arg)
    elif opt == "--start-constr":
      checkFormalismForTrees(settingType)
      startConstr = parseConstraints(arg)
    elif opt == "--end-constr":
      checkFormalismForTrees(settingType)
      endConstr = parseConstraints(arg)
    else:
      print("Unhandled option: " + opt)
      sys.exit(1)

  if (len(nodeConstr) == 0 and settingType != Type.TREE) or len(edgeConstr) == 0:
    print("Both node and edge constraints need to be non-empty")
    sys.exit(1)

  if settingType == "":
    print("Type option needs to be specified.")
    sys.exit(1)

  problem = Problem(nodeConstr, edgeConstr, startConstr, endConstr, settingType)
  
  result = classify(problem)
  print('Round complexity of the problem is %s' % result['complexity'])
  print(
    'Deciding the number of solvable instances is NP-complete' if
    result['solvable'] == HARD else
    'There are %s solvable instances' % result['solvable']
  )
  print(
    'Deciding the number of unsolvable instances is NP-complete' if
    result['unsolvable'] == HARD else
    'There are %s unsolvable instances' % result['unsolvable']
  )

  sys.exit(0)
      
if __name__ == "__main__":
   main()
