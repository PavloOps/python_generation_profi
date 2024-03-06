def pairwise(iterable):
    if iterable:
        sequence = iter(iterable)
        prev = next(sequence)
        yield from ((prev, i, prev := i)[:-1] for i in sequence)
        yield prev, None
    else:
        return []