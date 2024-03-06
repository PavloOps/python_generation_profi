def around(iterable):
    if iterable:
        sequence = iter(iterable)
        prev, curr = None, next(sequence)

        try:
            following = next(sequence)
        except StopIteration:
            yield prev, curr, prev

        yield prev, curr, following
        prev, curr = curr, following

        try:
            for following in sequence:
                yield prev, curr, following
                prev, curr = curr, following
            else:
                yield prev, curr, None
        except StopIteration:
            yield curr, following, None


    else:
        return []

def around(iterable):
    iterable = iter(iterable)
    fir, sec = None, next(iterable, None)
    while sec is not None:
        yield (fir, fir:=sec, sec:=next(iterable, None))