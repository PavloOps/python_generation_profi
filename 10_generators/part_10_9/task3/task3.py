from itertools import filterfalse


def first_true(iterable, predicate):
    for item in filterfalse(lambda x: not predicate(x) if predicate is not None else not bool(x), iterable):
        return item