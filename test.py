#!/usr/bin/python3

import unittest
from graph import *
from problem import *

class TestProblem(unittest.TestCase):
  vertex3Coloring = Problem(nodeConstr=["11", "22", "33"], edgeConstr=["12", "21", "13", "31", "23", "32"], startConstr=[], endConstr=[])
  edge3Coloring = Problem(nodeConstr=["12", "21", "13", "31", "23", "32"], edgeConstr=["11", "22", "33"], startConstr=[], endConstr=[])
  consistentOrientation = Problem(nodeConstr=["HT", "TH"], edgeConstr=["HT", "TH"], startConstr=[], endConstr=[])
  maximalMatching = Problem(nodeConstr=["00", "1M", "M1"], edgeConstr=["01", "10", "11", "MM"], startConstr=[], endConstr=[])
  assymSample = Problem(nodeConstr=["00", "1M"], edgeConstr=["01", "10", "11", "MM"], startConstr=[], endConstr=[])

  def testToGraph(self):
    self.assertDictEqual(toGraph(self.vertex3Coloring), { "12": ["21", "23"], "13": ["31", "32"], "21": ["12", "13"], "23": ["31", "32"], "31": ["12", "13"], "32": ["21", "23"] })
    self.assertDictEqual(toGraph(self.edge3Coloring), { "11": ["22", "33"], "22": ["11", "33"], "33": ["11", "22"] })
    self.assertDictEqual(toGraph(self.consistentOrientation), { "HT": ["HT"], "TH": ["TH"] })
    self.assertDictEqual(toGraph(self.maximalMatching), { "11": ["MM"], "10": ["01"], "01": ["MM"], "MM": ["10", "11"] })

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

unittest.main()
