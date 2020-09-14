from complexity import complexities
from problem import isSymmetric, toGraph
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

  return complexities["cycles"]["undirected"][problemType]
  

