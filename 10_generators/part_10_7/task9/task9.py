# def stop_on(iterable, obj):
#     for item in iterable:
#         if item == obj:
#             break
#         else:
#             yield item
#

def stop_on(iterable, obj):
    it = iter(iterable)
    return iter(lambda: next(it), obj)