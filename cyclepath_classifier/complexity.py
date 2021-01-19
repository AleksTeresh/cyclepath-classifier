from .problem import Type

CONST = "O(1)"
GLOBAL = "Θ(n)"
ITERATED_LOG = "Θ(log* n)"
UNSOLVABLE = " - "

complexities = {
  "cycles": {
    Type.DIRECTED: {
      "A": CONST,
      "B": CONST,
      "C": CONST,
      "D": CONST,
      "E": ITERATED_LOG,
      "F": ITERATED_LOG,
      "G": ITERATED_LOG,
      "H": GLOBAL,
      "I": GLOBAL,
      "J": UNSOLVABLE,
      "K": UNSOLVABLE,
    },
    Type.UNDIRECTED: {
      "A": CONST,
      "B": ITERATED_LOG,
      "C": GLOBAL,
      "D": GLOBAL,
      "E": ITERATED_LOG,
      "F": GLOBAL,
      "G": GLOBAL,
      "H": GLOBAL,
      "I": GLOBAL,
      "J": UNSOLVABLE,
      "K": UNSOLVABLE,
    }
  },
  "paths": {
    Type.DIRECTED: {
      "A": CONST,
      "B": CONST,
      "C": CONST,
      "D": CONST,
      "E": ITERATED_LOG,
      "F": ITERATED_LOG,
      "G": ITERATED_LOG,
      "H": GLOBAL,
      "I": GLOBAL,
      "J": UNSOLVABLE,
      "K": CONST,
    },
    Type.UNDIRECTED: {
      "A": CONST,
      "B": ITERATED_LOG,
      "C": GLOBAL,
      "D": GLOBAL,
      "E": ITERATED_LOG,
      "F": GLOBAL,
      "G": GLOBAL,
      "H": GLOBAL,
      "I": GLOBAL,
      "J": UNSOLVABLE,
      "K": CONST,
    }
  }
}
