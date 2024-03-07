from itertools import cycle, islice


def roundrobin(*args):
    num_active = len(args)
    nexts = cycle(iter(it).__next__ for it in args)

    while num_active:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            # Remove the iterator we just exhausted from the cycle.
            num_active -= 1
            nexts = cycle(islice(nexts, num_active))
