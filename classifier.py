#!/usr/bin/python3

import sys, getopt
from complexity import complexities
from instances import instanceCounts, HARD
from problem import isSymmetric, toGraph, Problem, Type
from graph import hasRepeatable, hasFlexible, hasLoop, hasMirrorFlexible, hasMirrorFlexibleLoop
from util import flatMap

def classify(problem):
  graph = toGraph(problem)

  s = isSymmetric(problem)
  if not s and problem.type != Type.UNDIRECTED:
    print("A problem has to be of 'undirected' type if its constraints are asymmetric. Otherwise it is not well-defined.")
    return

  r = hasRepeatable(graph)
  f = hasFlexible(graph)
  l = hasLoop(graph)
  mf = hasMirrorFlexible(graph)
  mfl = hasMirrorFlexibleLoop(graph)

  if s and r and f and l and mf and mfl:
    problemType = "A"
  elif s and r and f and l and mf and not mfl:
    problemType = "B"
  elif s and r and f and l and not mf and not mfl:
    problemType = "C"
  elif not s and r and f and l and not mf and not mfl:
    problemType = "D"
  elif s and r and f and not l and mf and not mfl:
    problemType = "E"
  elif s and r and f and not l and not mf and not mfl:
    problemType = "F"
  elif not s and r and f and not l and not mf and not mfl:
    problemType = "G"
  elif s and r and not f and not l and not mf and not mfl:
    problemType = "H"
  elif not s and r and not f and not l and not mf and not mfl:
    problemType = "I"
  elif s and not r and not f and not l and not mf and not mfl:
    problemType = "J"
  elif not s and not r and not f and not l and not mf and not mfl:
    problemType = "K"
  else:
    print("No problem type matches the specified problem.")
    raise Exception

  setting = "paths" if problem.startConstr or problem.endConstr else "cycles"
  # complexity on a tree is the same as on a directed path
  orientation = Type.DIRECTED if problem.type == Type.TREE else problem.type

  complexity = complexities[setting][orientation][problemType]
  solvableInstanceCount = instanceCounts[setting][problemType]["solvable"]
  unsolvableInstanceCount = instanceCounts[setting][problemType]["unsolvable"]

  print('Round complexity of the problem is %s' % complexity)
  print(
    'Deciding the number of solvable instances is NP-complete' if
    solvableInstanceCount == "HARD" else
    'There are %s solvable instances' % solvableInstanceCount
  )
  print(
    'Deciding the number of unsolvable instances is NP-complete' if
    solvableInstanceCount == "HARD" else
    'There are %s unsolvable instances' % unsolvableInstanceCount
  )

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
  startConstr={}
  endConstr={}
  settingType=""

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
  elif settingType == Type.TREE:
    alphabet = set(flatMap(lambda x: x, edgeConstr))
    nodeConstr = set(map(lambda x: x + x, alphabet))
    startConstr = alphabet
    endConstr = alphabet

  problem = Problem(nodeConstr, edgeConstr, startConstr, endConstr, settingType)
  
  try:
    classify(problem)
  except:
    print("Something went wrong...")
    sys.exit(1)

  sys.exit(0)
      
if __name__ == "__main__":
   main()
