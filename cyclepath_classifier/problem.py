from functools import reduce
from typing import NamedTuple, Set
from enum import Enum
from .graph import prune

class Type(Enum):
  DIRECTED = 1
  UNDIRECTED = 2
  TREE = 3

class Problem(NamedTuple):
  nodeConstr: Set[str]
  edgeConstr: Set[str]
  startConstr: Set[str]
  endConstr: Set[str]
  type: Type

def isSymmetric(problem):
  symmetricEdges = reduce(lambda acc, x: acc and (x[::-1] in problem.edgeConstr), problem.edgeConstr, True)
  symmetricNodes = reduce(lambda acc, x: acc and (x[::-1] in problem.nodeConstr), problem.nodeConstr, True)
  symmetricEnds = set(problem.startConstr) == set(problem.endConstr)
  return symmetricEdges and symmetricNodes and symmetricEnds

def toGraph(problem):
  graph = {x: [] for x in problem.edgeConstr}
  for constr in problem.nodeConstr:
    b = constr[0]
    c = constr[1]
    for key1 in graph:
      for key2 in graph:
        if key1[1] == b and key2[0] == c:
          graph[key1].append(key2)

  startingStates = set(filter(lambda x: x[0] in problem.startConstr, problem.edgeConstr))
  acceptingStates = set(filter(lambda x: x[1] in problem.endConstr, problem.edgeConstr))

  return prune(graph, startingStates, acceptingStates) if startingStates or acceptingStates else graph
