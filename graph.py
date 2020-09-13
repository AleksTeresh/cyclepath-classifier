from math import gcd
from functools import reduce

graphA = {"12": ["34"], "21": ["12"], "34": ["34", "43"], "43": ["43", "21"]}
graphB = {"12": ["12"], "21": ["21"], "33": ["44", "55"], "44": ["33", "55"], "55": ["33", "44"]}
graphC = {"12": ["12"], "21": ["21"]}
graphD = {"12": ["12"]}
graphE = {"11": ["22", "33"], "22": ["11", "33"], "33": ["11", "22"]}
graphF = {"12": ["34", "56"], "34": ["12", "56"], "56": ["12", "34"], "21": ["43", "65"], "43": ["21", "65"], "65": ["21", "43"]}
graphG = {"12": ["34", "56"], "34": ["12", "56"], "56": ["12", "34"]}
graphH = {"11": ["22"], "22": ["11"]}
graphI = {"12": ["34"], "34": ["12"]}
graphJ = {"12": ["34"], "34": [], "43": ["21"], "21": []}
graphK = {"12": ["34"], "34": []}

def listGcd(arr):
  return reduce(gcd, arr)

def countWalks(graph, src, dst, maxWalkLength):
  # Table to be filled up using DP. 
  # The value count[i][j][e] will 
  # store count of possible walks from 
  # i to j with exactly k edges 
  count = {i: {j : [0 for k in range(maxWalkLength + 1)] for j in graph} for i in graph}

  # Loop for number of edges from 0 to k 
  for e in range(maxWalkLength + 1):
    for i in graph: # for source 
      for j in graph: # for destination 
        # initialize value 
        count[i][j][e] = 0

        # from base cases 
        if e == 0 and i == j:
          count[i][j][e] = 1
        if e == 1 and (j in graph[i]):
          count[i][j][e] = 1

        # go to adjacent only when the 
        # number of edges is more than 1 
        if e > 1:
          for a in graph:
            if a in graph[i]: # adjacent of source i 
              count[i][j][e] += count[a][j][e - 1]
        
  return count[src][dst]

def hasProperty(graph, propPredicate):
  return reduce(lambda acc, x: acc or propPredicate(graph, x), graph, False)

def isReachable(graph, src, dst):
  return len(list(filter(lambda x: x > 0, countWalks(graph, src, dst, len(graph))[1:]))) > 0

def isRepeatable(graph, node):
  return isReachable(graph, node, node)

def hasRepeatable(graph):
  return hasProperty(graph, isRepeatable)

def isFlexible(graph, node):
  walkCounts = countWalks(graph, node, node, 2 * len(graph))
  bigL = []
  for idx, count in enumerate(walkCounts):
    if idx > 0 and count > 0: # disregard a walk with 0 edges
      bigL.append(idx)

  return len(bigL) > 0 and listGcd(bigL) == 1

def hasFlexible(graph):
  return hasProperty(graph, isFlexible)

def isLoop(graph, node):
  return node in graph[node]

def hasLoop(graph):
  return hasProperty(graph, isLoop)

def getMirror(graph, node):
  return str(node)[::-1]

def hasMirror(graph, node):
  mirror = getMirror(graph, node)
  return mirror in graph

def isMirrorFlexible(graph, node):
  if hasMirror(graph, node):
    mirror = getMirror(graph, node)
    return (isFlexible(graph, node) and
            isReachable(graph, node, mirror) and
            isReachable(graph, mirror, node))
  else:
    return False

def hasMirrorFlexible(graph):
  return hasProperty(graph, isMirrorFlexible)

def isMirrorFlexibleLoop(graph, node):
  return isMirrorFlexible(graph, node) and isLoop(graph, node)

def hasMirrorFlexibleLoop(graph):
  return hasProperty(graph, isMirrorFlexibleLoop)
