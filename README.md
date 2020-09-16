# Cyclepath classifier

A command-line tool for automatically calculating round complexity of LCL problems in cycles and paths based on their description in the node-edge-checkable formalism. It also reports the number of solvable/unsolvable instances of a problem when classifying it (see examples below).

The tool is based on the techniques described in [this paper](https://arxiv.org/abs/2002.07659).

## Requirements

* Python 3.8.3 or later version

## Getting started

_NOTE: For now the tool assumes that the problem is always specified for a directed cycle/path. Support for undirected cycles and paths will be added later._

Run the tool specifying node and edge constraints of a problem in the node-edge-checkable formalism.

The required parameters are `-n` or `--node-constr` and `-e` or `--edge-constr`.
There are also optional parameters specifying start and end constraints: `--start-constr` and `--end-constr`

The tool will assume that the problem is defined for a **path** if either `--start-constr` or `--end-constr` is specified. Otherwise, **cycle** setting is assumed.

### Examples

```
$ ./classifier.py -n "{ 11, 22, 33 }" -e "{ 12, 21, 13, 31, 23, 32 }"

Round complexity of the problem is Θ(log* n)
There are infinitely many solvable instances
There are finitely many unsolvable instances
```

```
$ ./classifier.py -n "{ 00, 1M, M1 }" -e "{ 01, 10, 11, MM }"

Round complexity of the problem is Θ(log* n)
There are infinitely many solvable instances
There are finitely many unsolvable instances
```

```
$ ./classifier.py -n "{ HT, TH }" -e "{ HT, TH }"

Round complexity of the problem is O(1)
There are infinitely many solvable instances
There are 0 unsolvable instances
```

```
$ ./classifier.py -n "{ 12, 21 }" -e "{ 11, 22 }"

Round complexity of the problem is Θ(n)
There are infinitely many solvable instances
There are infinitely many unsolvable instances
```

```
$ ./classifier.py -n "{00, 1M}" -e "{01, 10, 11, MM}" --start-constr "{ 1 }" --end-constr "{ 1 }"

Round complexity of the problem is O(1)
There are finitely many solvable instances
There are infinitely many unsolvable instances
```

## Tests

Run tests with `./test.py`. See the file for details.
