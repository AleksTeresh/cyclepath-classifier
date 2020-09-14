#!/usr/bin/python3

import sys, getopt
from complexity import complexities
from problem import isSymmetric, toGraph, Problem
from graph import hasRepeatable, hasFlexible, hasLoop, hasMirrorFlexible, hasMirrorFlexibleLoop

def classify(problem):
  graph = toGraph(problem)

  s = isSymmetric(problem)
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
    print("No problem type matches problem.")
    raise Exception

  return complexities["cycles"]["directed"][problemType]

def usage():
  print('classifier.py -n {<node constraint 1>, <node constraint 2>, ...} -e {<edge constraint 1>, ...}')

def main():
  try:
    opts, args = getopt.getopt(sys.argv[1:],"hn:e:",["help", "node-constr=","edge-constr="])
  except getopt.GetoptError as err:
    print(err)
    usage()
    sys.exit(2)

  for opt, arg in opts:
    if opt in ("-h", "--help"):
      usage()
      sys.exit()
    elif opt in ("-n", "--node-constr"):
      try :
        nodeConstr = set(map(lambda x: x.strip(), arg.strip()[1:-1].split(',')))
      except ValueError:
        print("Specify constraints in the following format: {<node constraint 1>, <node constraint 2>, ...}")
        sys.exit(1)
    elif opt in ("-e", "--edge-constr"):
      try :
        edgeConstr = set(map(lambda x: x.strip(), arg.strip()[1:-1].split(',')))
      except ValueError:
        print("Specify constraints in the following format: {<edge constraint 1>, <edge constraint 2>, ...}")
        sys.exit(1)
    else:
      print("Unhandled option: " + opt)
      sys.exit(1)

  if len(nodeConstr) == 0 or len(edgeConstr) == 0:
    print("Both node and edge constraints need to be non-empty")
    sys.exit(1)

  problem = Problem(nodeConstr, edgeConstr, {}, {})
  
  try:
    complexity = classify(problem)
  except:
    print("Something went wrong...")
    sys.exit(1)

  print('Round complexity of the problem is ' + complexity)
  sys.exit(0)
      
if __name__ == "__main__":
   main()
