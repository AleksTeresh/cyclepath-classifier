#!/usr/bin/python3

from .complexity import complexities
from .instances import instanceCounts
from .problem import isSymmetric, toGraph, Problem, Type
from .util import flatMap
from .graph import hasRepeatable, hasFlexible, hasLoop, hasMirrorFlexible, hasMirrorFlexibleLoop

def preprocessProblem(problem):
  if problem.type == Type.TREE:
    alphabet = set(flatMap(lambda x: x, problem.edgeConstr))
    nodeConstr = set(map(lambda x: x + x, alphabet))
    startConstr = alphabet
    endConstr = alphabet
    return Problem(
      nodeConstr,
      problem.edgeConstr,
      startConstr,
      endConstr,
      problem.type
    )
  else:
    return problem

def classify(problem):
  problem = preprocessProblem(problem)

  graph = toGraph(problem)

  s = isSymmetric(problem)
  if not s and problem.type == Type.UNDIRECTED:
    raise Exception("A problem cannot be of 'undirected' type if its constraints are asymmetric. Otherwise it is not well-defined.")

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
  elif not s and r and f and l:
    problemType = "D"
  elif s and r and f and not l and mf and not mfl:
    problemType = "E"
  elif s and r and f and not l and not mf and not mfl:
    problemType = "F"
  elif not s and r and f and not l:
    problemType = "G"
  elif s and r and not f and not l and not mf and not mfl:
    problemType = "H"
  elif not s and r and not f and not l:
    problemType = "I"
  elif s and not r and not f and not l and not mf and not mfl:
    problemType = "J"
  elif not s and not r and not f and not l:
    problemType = "K"
  else:
    raise Exception("No problem type matches the specified problem.")

  setting = "paths" if problem.startConstr or problem.endConstr else "cycles"
  # complexity on a tree is the same as on a directed path
  orientation = Type.DIRECTED if problem.type == Type.TREE else problem.type

  complexity = complexities[setting][orientation][problemType]
  solvableInstanceCount = instanceCounts[setting][problemType]["solvable"]
  unsolvableInstanceCount = instanceCounts[setting][problemType]["unsolvable"]

  return {
    'complexity': complexity,
    'solvable': solvableInstanceCount,
    'unsolvable': unsolvableInstanceCount
  }
