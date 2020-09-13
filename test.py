import unittest
from graph import *

class TestAutomataProps(unittest.TestCase):
  def testA(self):
    self.assertTrue(hasRepeatable(graphA))
    self.assertTrue(isRepeatable(graphA, "12"))
    self.assertTrue(isRepeatable(graphA, "21"))
    self.assertTrue(isRepeatable(graphA, "34"))
    self.assertTrue(isRepeatable(graphA, "43"))

    self.assertTrue(hasFlexible(graphA))
    self.assertTrue(isFlexible(graphA, "12"))
    self.assertTrue(isFlexible(graphA, "21"))
    self.assertTrue(isFlexible(graphA, "34"))
    self.assertTrue(isFlexible(graphA, "43"))

    self.assertTrue(hasLoop(graphA))
    self.assertTrue(isLoop(graphA, "34"))
    self.assertTrue(isLoop(graphA, "43"))

    self.assertTrue(hasMirrorFlexible(graphA))
    self.assertTrue(isMirrorFlexible(graphA, "12"))
    self.assertTrue(isMirrorFlexible(graphA, "21"))
    self.assertTrue(isMirrorFlexible(graphA, "34"))
    self.assertTrue(isMirrorFlexible(graphA, "43"))

    self.assertTrue(hasMirrorFlexibleLoop(graphA))
    self.assertTrue(isMirrorFlexibleLoop(graphA, "34"))
    self.assertTrue(isMirrorFlexibleLoop(graphA, "43"))

  def testB(self):
    self.assertTrue(hasRepeatable(graphB))
    self.assertTrue(isRepeatable(graphB, "12"))
    self.assertTrue(isRepeatable(graphB, "21"))
    self.assertTrue(isRepeatable(graphB, "33"))
    self.assertTrue(isRepeatable(graphB, "44"))
    self.assertTrue(isRepeatable(graphB, "55"))

    self.assertTrue(hasFlexible(graphB))
    self.assertTrue(isFlexible(graphB, "12"))
    self.assertTrue(isFlexible(graphB, "21"))
    self.assertTrue(isFlexible(graphB, "33"))
    self.assertTrue(isFlexible(graphB, "44"))
    self.assertTrue(isFlexible(graphB, "55"))

    self.assertTrue(hasLoop(graphB))
    self.assertTrue(isLoop(graphB, "12"))
    self.assertTrue(isLoop(graphB, "21"))

    self.assertTrue(hasMirrorFlexible(graphB))
    self.assertTrue(isMirrorFlexible(graphB, "33"))
    self.assertTrue(isMirrorFlexible(graphB, "44"))
    self.assertTrue(isMirrorFlexible(graphB, "55"))

    self.assertFalse(hasMirrorFlexibleLoop(graphB))

  def testC(self):
    self.assertTrue(hasRepeatable(graphC))
    self.assertTrue(isRepeatable(graphC, "12"))
    self.assertTrue(isRepeatable(graphC, "21"))

    self.assertTrue(hasFlexible(graphC))
    self.assertTrue(isFlexible(graphC, "12"))
    self.assertTrue(isFlexible(graphC, "21"))

    self.assertTrue(hasLoop(graphC))
    self.assertTrue(isLoop(graphC, "12"))
    self.assertTrue(isLoop(graphC, "21"))

    self.assertFalse(hasMirrorFlexible(graphC))
    self.assertFalse(hasMirrorFlexibleLoop(graphC))

  def testD(self):
    self.assertTrue(hasRepeatable(graphD))
    self.assertTrue(isRepeatable(graphD, "12"))

    self.assertTrue(hasFlexible(graphD))
    self.assertTrue(isFlexible(graphD, "12"))

    self.assertTrue(hasLoop(graphD))
    self.assertTrue(isLoop(graphD, "12"))

    self.assertFalse(hasMirrorFlexible(graphD))
    self.assertFalse(hasMirrorFlexibleLoop(graphD))

  def testE(self):
    self.assertTrue(hasRepeatable(graphE))
    self.assertTrue(isRepeatable(graphE, "11"))
    self.assertTrue(isRepeatable(graphE, "22"))
    self.assertTrue(isRepeatable(graphE, "33"))

    self.assertTrue(hasFlexible(graphE))
    self.assertTrue(isFlexible(graphE, "11"))
    self.assertTrue(isFlexible(graphE, "22"))
    self.assertTrue(isFlexible(graphE, "33"))

    self.assertFalse(hasLoop(graphE))
    self.assertTrue(hasMirrorFlexible(graphE))
    self.assertTrue(isMirrorFlexible(graphE, "11"))
    self.assertTrue(isMirrorFlexible(graphE, "22"))
    self.assertTrue(isMirrorFlexible(graphE, "33"))

    self.assertFalse(hasMirrorFlexibleLoop(graphE))

  def testF(self):
    self.assertTrue(hasRepeatable(graphF))
    self.assertTrue(isRepeatable(graphF, "12"))
    self.assertTrue(isRepeatable(graphF, "34"))
    self.assertTrue(isRepeatable(graphF, "56"))
    self.assertTrue(isRepeatable(graphF, "21"))
    self.assertTrue(isRepeatable(graphF, "43"))
    self.assertTrue(isRepeatable(graphF, "65"))

    self.assertTrue(hasFlexible(graphF))
    self.assertTrue(isFlexible(graphF, "12"))
    self.assertTrue(isFlexible(graphF, "34"))
    self.assertTrue(isFlexible(graphF, "56"))
    self.assertTrue(isFlexible(graphF, "21"))
    self.assertTrue(isFlexible(graphF, "43"))
    self.assertTrue(isFlexible(graphF, "65"))

    self.assertFalse(hasLoop(graphF))
    self.assertFalse(hasMirrorFlexible(graphF))
    self.assertFalse(hasMirrorFlexibleLoop(graphF))

  def testG(self):
    self.assertTrue(hasRepeatable(graphG))
    self.assertTrue(isRepeatable(graphG, "12"))
    self.assertTrue(isRepeatable(graphG, "34"))
    self.assertTrue(isRepeatable(graphG, "56"))

    self.assertTrue(hasFlexible(graphG))
    self.assertTrue(isFlexible(graphG, "12"))
    self.assertTrue(isFlexible(graphG, "34"))
    self.assertTrue(isFlexible(graphG, "56"))

    self.assertFalse(hasLoop(graphG))
    self.assertFalse(hasMirrorFlexible(graphG))
    self.assertFalse(hasMirrorFlexibleLoop(graphG))

  def testH(self):
    self.assertTrue(hasRepeatable(graphH))
    self.assertTrue(isRepeatable(graphH, "11"))
    self.assertTrue(isRepeatable(graphH, "22"))

    self.assertFalse(hasFlexible(graphH))
    self.assertFalse(hasLoop(graphH))
    self.assertFalse(hasMirrorFlexible(graphH))
    self.assertFalse(hasMirrorFlexibleLoop(graphH))

  def testI(self):
    self.assertTrue(hasRepeatable(graphI))
    self.assertTrue(isRepeatable(graphI, "12"))
    self.assertTrue(isRepeatable(graphI, "34"))

    self.assertFalse(hasFlexible(graphI))
    self.assertFalse(hasLoop(graphI))
    self.assertFalse(hasMirrorFlexible(graphI))
    self.assertFalse(hasMirrorFlexibleLoop(graphI))

  def testJ(self):
    self.assertFalse(hasRepeatable(graphJ))
    self.assertFalse(hasFlexible(graphJ))
    self.assertFalse(hasLoop(graphJ))
    self.assertFalse(hasMirrorFlexible(graphJ))
    self.assertFalse(hasMirrorFlexibleLoop(graphJ))

  def testK(self):
    self.assertFalse(hasRepeatable(graphK))
    self.assertFalse(hasFlexible(graphK))
    self.assertFalse(hasLoop(graphK))
    self.assertFalse(hasMirrorFlexible(graphK))
    self.assertFalse(hasMirrorFlexibleLoop(graphK))

unittest.main()
