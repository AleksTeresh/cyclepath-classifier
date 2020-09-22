from functools import reduce

flatMap = lambda f, arr: reduce(lambda a, b: a + b, map(f, arr))
