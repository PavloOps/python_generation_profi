from itertools import count

def tabulate(func):
    for number in count(1, 1):
        yield func(number)
