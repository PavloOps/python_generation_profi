from itertools import cycle
from string import ascii_uppercase


def alnum_sequence():
    for tup in cycle(zip(range(1, 27), ascii_uppercase)):
        yield from tup
