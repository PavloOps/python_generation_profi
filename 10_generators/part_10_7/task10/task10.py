def with_previous(iterable):
    if not iterable:
        return []
    else:
        seq = iter(iterable)
        curr_item = next(seq)
        yield curr_item, None

    for previous_item in seq:
        yield previous_item, curr_item
        curr_item = previous_item

def with_previous(iterable):
    prev = None
    return ((i, prev, prev := i)[:-1] for i in iterable)

# iterator = iter('stepik')
#
# for item in with_previous(iterator):
#     print(item)