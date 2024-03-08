from itertools import islice


def take_nth(iterable, n):
    for ind, item in enumerate(islice(iterable, n), start=1):
        if ind == n:
            return item
    else:
        return None


def take_nth(iterable, n):
    return next(islice(iterable, n-1, n), None)