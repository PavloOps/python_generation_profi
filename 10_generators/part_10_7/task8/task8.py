def unique(iterable):
    cache = dict()

    for item in iterable:
        cache[item] = cache.get(item, 0) + 1

        if cache[item] > 1:
            continue
        else:
            yield item
