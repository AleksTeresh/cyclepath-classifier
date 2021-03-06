#!/usr/bin/python3

import unittest, subprocess, sys
from cyclepath_classifier import *

class TestE2E(unittest.TestCase):
  def testFastCycleProblem1(self):
    result = subprocess.run([sys.executable, '-m', 'cyclepath_classifier', '-t', 'undir', '-n', '{ 11, 22, 33}', "-e", "{ 12, 21, 13, 31, 23, 32 }"], capture_output=True)
    lines = str(result.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 4)
    self.assertEqual(lines[0], "Round complexity of the problem is Θ(log* n)")
    self.assertEqual(lines[1], "There are infinitely many solvable instances")
    self.assertEqual(lines[2], "There are finitely many unsolvable instances")
    self.assertEqual(lines[3], '')

  def testFastCycleProblem2(self):
    result = subprocess.run([sys.executable, '-m', 'cyclepath_classifier', '-t', 'undir', '-n', '{ 00, 1M, M1 }', "-e", "{ 01, 10, 11, MM }"], capture_output=True)
    lines = str(result.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 4)
    self.assertEqual(lines[0], "Round complexity of the problem is Θ(log* n)")
    self.assertEqual(lines[1], "There are infinitely many solvable instances")
    self.assertEqual(lines[2], "There are finitely many unsolvable instances")
    self.assertEqual(lines[3], '')

  def testTrivialCycleProblem(self):
    result = subprocess.run([sys.executable, '-m', 'cyclepath_classifier', '-t', 'dir', '-n', '{HT, TH}', "-e", "{HT, TH}"], capture_output=True)
    lines = str(result.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 4)
    self.assertEqual(lines[0], "Round complexity of the problem is O(1)")
    self.assertEqual(lines[1], "There are infinitely many solvable instances")
    self.assertEqual(lines[2], "There are 0 unsolvable instances")
    self.assertEqual(lines[3], '')

  def testGlobalCycleProblem(self):
    result = subprocess.run([sys.executable, '-m', 'cyclepath_classifier', '-t', 'undir', '-n', '{ 12, 21 }', "-e", "{ 11, 22 }"], capture_output=True)
    lines = str(result.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 4)
    self.assertEqual(lines[0], "Round complexity of the problem is Θ(n)")
    self.assertEqual(lines[1], "There are infinitely many solvable instances")
    self.assertEqual(lines[2], "There are infinitely many unsolvable instances")
    self.assertEqual(lines[3], '')

  def testGlobalDirectedCycleProblem(self):
    result = subprocess.run([sys.executable, '-m', 'cyclepath_classifier', '-t', 'dir', '-n', '{ 12, 21 }', "-e", "{ 11, 22 }"], capture_output=True)
    lines = str(result.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 4)
    self.assertEqual(lines[0], "Round complexity of the problem is Θ(n)")
    self.assertEqual(lines[1], "There are infinitely many solvable instances")
    self.assertEqual(lines[2], "There are infinitely many unsolvable instances")
    self.assertEqual(lines[3], '')

  def testTrivialPathProblem(self):
    result = subprocess.run([sys.executable, '-m', 'cyclepath_classifier', '-t', 'undir', '-n', '{00, 1M}', "-e", "{01, 10, 11, MM}", '--start-constr', '{ 1 }', '--end-constr', '{ 1 }'], capture_output=True)
    lines = str(result.stderr.decode('utf-8')).split('\n')

    self.assertIn("A problem cannot be of 'undirected' type if its constraints are asymmetric. Otherwise it is not well-defined.", lines[-2])
    self.assertEqual(lines[-1], "")

  def testAsymmetricDirected(self):
    result = subprocess.run([sys.executable, '-m', 'cyclepath_classifier', '-t', 'dir', '-n', '{00, 1M}', "-e", "{01, 10, 11, MM}", '--start-constr', '{ 1 }', '--end-constr', '{ 1 }'], capture_output=True)
    lines = str(result.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 4)
    self.assertEqual(lines[0], "Round complexity of the problem is O(1)")
    self.assertEqual(lines[1], "There are finitely many solvable instances")
    self.assertEqual(lines[2], "There are infinitely many unsolvable instances")
    self.assertEqual(lines[3], '')

  def testGracefulErrorForTree(self):
    result = subprocess.run([sys.executable, '-m', 'cyclepath_classifier', '-t', 'tree', '-n', '{ 12, 21 }', "-e", "{ 11, 22 }"], capture_output=True)
    lines = str(result.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 2)
    self.assertEqual(lines[0], "Do not specify any constraints other than edge-constr when --type option is 'tree'")
    self.assertEqual(lines[1], '')

  def testTreeAndDirectedPathEq1(self):
    result1 = subprocess.run([sys.executable, '-m', 'cyclepath_classifier', '-t', 'tree', '-e', '{ 11, 22 }'], capture_output=True)
    lines = str(result1.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 4)
    self.assertEqual(lines[0], "Round complexity of the problem is O(1)")
    self.assertEqual(lines[1], "There are infinitely many solvable instances")
    self.assertEqual(lines[2], "There are finitely many unsolvable instances")
    self.assertEqual(lines[3], '')

    result2 = subprocess.run([sys.executable, '-m', 'cyclepath_classifier', '-t', 'dir', '-n', '{11, 22}', '-e', '{ 11, 22 }', '--start-constr', '{ 1, 2 }', '--end-constr', '{ 1, 2 }'], capture_output=True)
    self.assertEqual(result1.stdout, result2.stdout)

  def testTreeAndDirectedPathEq2(self):
    result1 = subprocess.run([sys.executable, '-m', 'cyclepath_classifier', '-t', 'tree', "-e", "{ 01, 10, 11, MM }"], capture_output=True)
    lines = str(result1.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 4)
    self.assertEqual(lines[0], "Round complexity of the problem is O(1)")
    self.assertEqual(lines[1], "There are infinitely many solvable instances")
    self.assertEqual(lines[2], "There are finitely many unsolvable instances")
    self.assertEqual(lines[3], '')

    result2 = subprocess.run([sys.executable, '-m', 'cyclepath_classifier', '-t', 'dir', "-n", "{ 00, 11, MM }", "-e", "{ 01, 10, 11, MM }", '--start-constr', '{ 0, 1, M }', '--end-constr', '{ 0, 1, M }'], capture_output=True)
    self.assertEqual(result1.stdout, result2.stdout)

  def testTreeAndDirectedPathEq3(self):
    result1 = subprocess.run([sys.executable, '-m', 'cyclepath_classifier', '-t', 'tree', "-e", "{ 12, 21, 13, 31, 23, 32 }"], capture_output=True)
    lines = str(result1.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 4)
    self.assertEqual(lines[0], "Round complexity of the problem is Θ(log* n)")
    self.assertEqual(lines[1], "There are infinitely many solvable instances")
    self.assertEqual(lines[2], "There are finitely many unsolvable instances")
    self.assertEqual(lines[3], '')

    result2 = subprocess.run([sys.executable, '-m', 'cyclepath_classifier', '-t', 'dir', "-n", "{ 22, 11, 33 }", "-e", "{ 12, 21, 13, 31, 23, 32 }", '--start-constr', '{ 2, 1, 3 }', '--end-constr', '{ 2, 1, 3 }'], capture_output=True)
    self.assertEqual(result1.stdout, result2.stdout)

  def testTreeAndDirectedPathEq4(self):
    result1 = subprocess.run([sys.executable, '-m', 'cyclepath_classifier', '-t', 'tree', "-e", "{ 14, 41, 12, 21, 13, 31 }"], capture_output=True)
    lines = str(result1.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 4)
    self.assertEqual(lines[0], "Round complexity of the problem is Θ(n)")
    self.assertEqual(lines[1], "There are infinitely many solvable instances")
    self.assertEqual(lines[2], "Deciding the number of unsolvable instances is NP-complete")
    self.assertEqual(lines[3], '')

    result2 = subprocess.run([sys.executable, '-m', 'cyclepath_classifier', '-t', 'dir', "-n", "{ 22, 11, 33, 44 }", "-e", "{ 14, 41, 12, 21, 13, 31 }", '--start-constr', '{ 2, 1, 3, 4 }', '--end-constr', '{ 2, 1, 3, 4 }'], capture_output=True)
    self.assertEqual(result1.stdout, result2.stdout)

  def testTreeAndDirectedPathEq5(self):
    result1 = subprocess.run([sys.executable, '-m', 'cyclepath_classifier', '-t', 'tree', "-e", "{ 12, 21, 13 }"], capture_output=True)
    lines = str(result1.stdout.decode('utf-8')).split('\n')

    self.assertEqual(len(lines), 4)
    self.assertEqual(lines[0], "Round complexity of the problem is Θ(n)")
    self.assertEqual(lines[1], "There are infinitely many solvable instances")
    self.assertEqual(lines[2], "Deciding the number of unsolvable instances is NP-complete")
    self.assertEqual(lines[3], '')

    result2 = subprocess.run([sys.executable, '-m', 'cyclepath_classifier', '-t', 'dir', "-n", "{ 22, 11, 33 }", "-e", "{ 12, 21, 13 }", '--start-constr', '{ 2, 1, 3 }', '--end-constr', '{ 2, 1, 3 }'], capture_output=True)
    self.assertEqual(result1.stdout, result2.stdout)

class TestProblem(unittest.TestCase):
  vertex3Coloring = Problem(
    nodeConstr=["11", "22", "33"],
    edgeConstr=["12", "21", "13", "31", "23", "32"],
    startConstr=[],
    endConstr=[],
    type=Type.UNDIRECTED
  )
  edge3Coloring = Problem(
    nodeConstr=["12", "21", "13", "31", "23", "32"],
    edgeConstr=["11", "22", "33"],
    startConstr=[],
    endConstr=[],
    type=Type.UNDIRECTED
  )
  consistentOrientation = Problem(
    nodeConstr=["HT", "TH"],
    edgeConstr=["HT", "TH"],
    startConstr=[],
    endConstr=[],
    type=Type.UNDIRECTED
  )
  maximalMatching = Problem(
    nodeConstr=["00", "1M", "M1"],
    edgeConstr=["01", "10", "11", "MM"],
    startConstr=[],
    endConstr=[],
    type=Type.UNDIRECTED
  )
  
  assymSample = Problem(
    nodeConstr=["00", "1M"],
    edgeConstr=["01", "10", "11", "MM"],
    startConstr=[],
    endConstr=[],
    type=Type.UNDIRECTED
  )
  prunableSample = Problem(
    nodeConstr=["00", "1M"],
    edgeConstr=["01", "10", "11", "MM"],
    startConstr=["1"],
    endConstr=["1"],
    type=Type.UNDIRECTED
  )

  def testToGraph(self):
    self.assertDictEqual(toGraph(self.vertex3Coloring), { "12": ["21", "23"], "13": ["31", "32"], "21": ["12", "13"], "23": ["31", "32"], "31": ["12", "13"], "32": ["21", "23"] })
    self.assertDictEqual(toGraph(self.edge3Coloring), { "11": ["22", "33"], "22": ["11", "33"], "33": ["11", "22"] })
    self.assertDictEqual(toGraph(self.consistentOrientation), { "HT": ["HT"], "TH": ["TH"] })
    self.assertDictEqual(toGraph(self.maximalMatching), { "11": ["MM"], "10": ["01"], "01": ["MM"], "MM": ["10", "11"] })
    
    self.assertDictEqual(toGraph(self.assymSample), { "11": ["MM"], "10": ["01"], "01": ["MM"], "MM": [] })

  def testGraphPruning(self):
    self.assertDictEqual(toGraph(self.prunableSample), { "11": [], "10": ["01"], "01": []})

  def testIsSymmetric(self):
    self.assertTrue(isSymmetric(self.vertex3Coloring))
    self.assertTrue(isSymmetric(self.edge3Coloring))
    self.assertTrue(isSymmetric(self.consistentOrientation))
    self.assertTrue(isSymmetric(self.maximalMatching))
    self.assertFalse(isSymmetric(self.assymSample))

class TestAutomataProps(unittest.TestCase):
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

  def testA(self):
    self.assertTrue(hasRepeatable(self.graphA))
    self.assertTrue(isRepeatable(self.graphA, "12"))
    self.assertTrue(isRepeatable(self.graphA, "21"))
    self.assertTrue(isRepeatable(self.graphA, "34"))
    self.assertTrue(isRepeatable(self.graphA, "43"))

    self.assertTrue(hasFlexible(self.graphA))
    self.assertTrue(isFlexible(self.graphA, "12"))
    self.assertTrue(isFlexible(self.graphA, "21"))
    self.assertTrue(isFlexible(self.graphA, "34"))
    self.assertTrue(isFlexible(self.graphA, "43"))

    self.assertTrue(hasLoop(self.graphA))
    self.assertTrue(isLoop(self.graphA, "34"))
    self.assertTrue(isLoop(self.graphA, "43"))

    self.assertTrue(hasMirrorFlexible(self.graphA))
    self.assertTrue(isMirrorFlexible(self.graphA, "12"))
    self.assertTrue(isMirrorFlexible(self.graphA, "21"))
    self.assertTrue(isMirrorFlexible(self.graphA, "34"))
    self.assertTrue(isMirrorFlexible(self.graphA, "43"))

    self.assertTrue(hasMirrorFlexibleLoop(self.graphA))
    self.assertTrue(isMirrorFlexibleLoop(self.graphA, "34"))
    self.assertTrue(isMirrorFlexibleLoop(self.graphA, "43"))

  def testB(self):
    self.assertTrue(hasRepeatable(self.graphB))
    self.assertTrue(isRepeatable(self.graphB, "12"))
    self.assertTrue(isRepeatable(self.graphB, "21"))
    self.assertTrue(isRepeatable(self.graphB, "33"))
    self.assertTrue(isRepeatable(self.graphB, "44"))
    self.assertTrue(isRepeatable(self.graphB, "55"))

    self.assertTrue(hasFlexible(self.graphB))
    self.assertTrue(isFlexible(self.graphB, "12"))
    self.assertTrue(isFlexible(self.graphB, "21"))
    self.assertTrue(isFlexible(self.graphB, "33"))
    self.assertTrue(isFlexible(self.graphB, "44"))
    self.assertTrue(isFlexible(self.graphB, "55"))

    self.assertTrue(hasLoop(self.graphB))
    self.assertTrue(isLoop(self.graphB, "12"))
    self.assertTrue(isLoop(self.graphB, "21"))

    self.assertTrue(hasMirrorFlexible(self.graphB))
    self.assertTrue(isMirrorFlexible(self.graphB, "33"))
    self.assertTrue(isMirrorFlexible(self.graphB, "44"))
    self.assertTrue(isMirrorFlexible(self.graphB, "55"))

    self.assertFalse(hasMirrorFlexibleLoop(self.graphB))

  def testC(self):
    self.assertTrue(hasRepeatable(self.graphC))
    self.assertTrue(isRepeatable(self.graphC, "12"))
    self.assertTrue(isRepeatable(self.graphC, "21"))

    self.assertTrue(hasFlexible(self.graphC))
    self.assertTrue(isFlexible(self.graphC, "12"))
    self.assertTrue(isFlexible(self.graphC, "21"))

    self.assertTrue(hasLoop(self.graphC))
    self.assertTrue(isLoop(self.graphC, "12"))
    self.assertTrue(isLoop(self.graphC, "21"))

    self.assertFalse(hasMirrorFlexible(self.graphC))
    self.assertFalse(hasMirrorFlexibleLoop(self.graphC))

  def testD(self):
    self.assertTrue(hasRepeatable(self.graphD))
    self.assertTrue(isRepeatable(self.graphD, "12"))

    self.assertTrue(hasFlexible(self.graphD))
    self.assertTrue(isFlexible(self.graphD, "12"))

    self.assertTrue(hasLoop(self.graphD))
    self.assertTrue(isLoop(self.graphD, "12"))

    self.assertFalse(hasMirrorFlexible(self.graphD))
    self.assertFalse(hasMirrorFlexibleLoop(self.graphD))

  def testE(self):
    self.assertTrue(hasRepeatable(self.graphE))
    self.assertTrue(isRepeatable(self.graphE, "11"))
    self.assertTrue(isRepeatable(self.graphE, "22"))
    self.assertTrue(isRepeatable(self.graphE, "33"))

    self.assertTrue(hasFlexible(self.graphE))
    self.assertTrue(isFlexible(self.graphE, "11"))
    self.assertTrue(isFlexible(self.graphE, "22"))
    self.assertTrue(isFlexible(self.graphE, "33"))

    self.assertFalse(hasLoop(self.graphE))
    self.assertTrue(hasMirrorFlexible(self.graphE))
    self.assertTrue(isMirrorFlexible(self.graphE, "11"))
    self.assertTrue(isMirrorFlexible(self.graphE, "22"))
    self.assertTrue(isMirrorFlexible(self.graphE, "33"))

    self.assertFalse(hasMirrorFlexibleLoop(self.graphE))

  def testF(self):
    self.assertTrue(hasRepeatable(self.graphF))
    self.assertTrue(isRepeatable(self.graphF, "12"))
    self.assertTrue(isRepeatable(self.graphF, "34"))
    self.assertTrue(isRepeatable(self.graphF, "56"))
    self.assertTrue(isRepeatable(self.graphF, "21"))
    self.assertTrue(isRepeatable(self.graphF, "43"))
    self.assertTrue(isRepeatable(self.graphF, "65"))

    self.assertTrue(hasFlexible(self.graphF))
    self.assertTrue(isFlexible(self.graphF, "12"))
    self.assertTrue(isFlexible(self.graphF, "34"))
    self.assertTrue(isFlexible(self.graphF, "56"))
    self.assertTrue(isFlexible(self.graphF, "21"))
    self.assertTrue(isFlexible(self.graphF, "43"))
    self.assertTrue(isFlexible(self.graphF, "65"))

    self.assertFalse(hasLoop(self.graphF))
    self.assertFalse(hasMirrorFlexible(self.graphF))
    self.assertFalse(hasMirrorFlexibleLoop(self.graphF))

  def testG(self):
    self.assertTrue(hasRepeatable(self.graphG))
    self.assertTrue(isRepeatable(self.graphG, "12"))
    self.assertTrue(isRepeatable(self.graphG, "34"))
    self.assertTrue(isRepeatable(self.graphG, "56"))

    self.assertTrue(hasFlexible(self.graphG))
    self.assertTrue(isFlexible(self.graphG, "12"))
    self.assertTrue(isFlexible(self.graphG, "34"))
    self.assertTrue(isFlexible(self.graphG, "56"))

    self.assertFalse(hasLoop(self.graphG))
    self.assertFalse(hasMirrorFlexible(self.graphG))
    self.assertFalse(hasMirrorFlexibleLoop(self.graphG))

  def testH(self):
    self.assertTrue(hasRepeatable(self.graphH))
    self.assertTrue(isRepeatable(self.graphH, "11"))
    self.assertTrue(isRepeatable(self.graphH, "22"))

    self.assertFalse(hasFlexible(self.graphH))
    self.assertFalse(hasLoop(self.graphH))
    self.assertFalse(hasMirrorFlexible(self.graphH))
    self.assertFalse(hasMirrorFlexibleLoop(self.graphH))

  def testI(self):
    self.assertTrue(hasRepeatable(self.graphI))
    self.assertTrue(isRepeatable(self.graphI, "12"))
    self.assertTrue(isRepeatable(self.graphI, "34"))

    self.assertFalse(hasFlexible(self.graphI))
    self.assertFalse(hasLoop(self.graphI))
    self.assertFalse(hasMirrorFlexible(self.graphI))
    self.assertFalse(hasMirrorFlexibleLoop(self.graphI))

  def testJ(self):
    self.assertFalse(hasRepeatable(self.graphJ))
    self.assertFalse(hasFlexible(self.graphJ))
    self.assertFalse(hasLoop(self.graphJ))
    self.assertFalse(hasMirrorFlexible(self.graphJ))
    self.assertFalse(hasMirrorFlexibleLoop(self.graphJ))

  def testK(self):
    self.assertFalse(hasRepeatable(self.graphK))
    self.assertFalse(hasFlexible(self.graphK))
    self.assertFalse(hasLoop(self.graphK))
    self.assertFalse(hasMirrorFlexible(self.graphK))
    self.assertFalse(hasMirrorFlexibleLoop(self.graphK))

# unittest.main()
