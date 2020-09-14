# Cyclepath classifier

A command-line tool for automatically calculating round complexity of LCL problems in cycles and paths based on their description in the node-edge-checkable formalism.

The tool is based on the techniques described in [this paper](https://arxiv.org/abs/2002.07659).

## Requirements

* Python 3.8.3 or later version

## Getting started

_NOTE: For now the tool assumes that the problem is always specified for a directed cycle. Support for undirected cycles and directed/undirected paths will be added later._

Run the tool specifying node and edge constraints of a problem in the node-edge-checkable formalism.

The allowed parameters are `-n` or `--node-constr` and `-e` or `--edge-constr`.

### Examples

```
$ ./classifier.py -n "{ 11, 22, 33 }" -e "{ 12, 21, 13, 31, 23, 32 }"

Round complexity of the problem is Θ(log* n)
```

```
$ ./classifier.py -n "{ 00, 1M, M1 }" -e "{ 01, 10, 11, MM }"

Round complexity of the problem is Θ(log* n)
```

```
$ ./classifier.py -n "{ HT, TH }" -e "{ HT, TH }"

Round complexity of the problem is O(1)
```

```
./classifier.py -n "{ 12, 21 }" -e "{ 11, 22 }"

Round complexity of the problem is Θ(n)
```

## Tests

Run tests with `./test.py`. See the file for details.
