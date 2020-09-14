from functools import reduce
from typing import NamedTuple, List

class Problem(NamedTuple):
  nodeConstr: List[str]
  edgeConstr: List[str]
  startConstr: List[str]
  endConstr: List[str]

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

  return graph
