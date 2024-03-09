from itertools import dropwhile, compress, count

def first_largest(iterable, number):
    res = next(dropwhile(lambda x: x[1] < number, enumerate(iterable)), -1)
    return res if isinstance(res, int) else res[0]

first_largest = lambda it, n: next(compress(count(), (i>n for i in it)), -1)
