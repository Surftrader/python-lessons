"""
NOTE: From Python 3.7+ all dict are ordered!

However OrderectDict is used for:
 - LRU-caching
 - realization limited queues and stacks where it is important to manage position of keys
"""

from collections import OrderedDict


od = OrderedDict()
od['a'] = 0
od['b'] = 2
od['d'] = 3
od['c'] = 4
od['a'] = 1

print(od)  # OrderedDict({'a': 1, 'b': 2, 'd': 3, 'c': 4})

od1 = OrderedDict([('key1', 1), ('key2', 'hello'), ('key3', True)])
od2 = OrderedDict((['key1', 1], ['key2', 'hello'], ['key3', True]))
od3 = OrderedDict(zip(['val1', 'val2', 'val3'], [1, 2, 3]))

print(od1)  # OrderedDict({'key1': 1, 'key2': 'hello', 'key3': True})
print(od2)  # OrderedDict({'key1': 1, 'key2': 'hello', 'key3': True})
print(od3)  # OrderedDict({'val1': 1, 'val2': 2, 'val3': 3})


d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'a': 1, 'c': 3}
print(d1 == d2)  # True

ord1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
ord2 = OrderedDict([('b', 2), ('a', 1), ('c', 3)])
print(ord1 == ord2)  # False

od1 = OrderedDict([('key1', 1), ('key2', 'hello'), ('key3', True)])
print(od1)  # OrderedDict({'key1': 1, 'key2': 'hello', 'key3': True})
od1.move_to_end('key2')
print(od1)  # OrderedDict({'key1': 1, 'key3': True, 'key2': 'hello'})
od1.move_to_end('key2', last=False)
print(od1)  # OrderedDict({'key2': 'hello', 'key1': 1, 'key3': True})
a = od1.popitem()
print(a)  # ('key3', True)
print(od1)  # OrderedDict({'key2': 'hello', 'key1': 1})
b = od1.popitem(last=False)
print(b)  # ('key2', 'hello')
print(od1)  # OrderedDict({'key1': 1})


class LRUCache(OrderedDict):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return None
        else:
            self.move_to_end(key, last=False)  # Move used key at the start
            return self[key]

    def put(self, key, value):
        if len(self) >= self.capacity:
            self.popitem()  # Delete the last (old) item
        self[key] = value  # add new item
        self.move_to_end(key, last=False)  # Move it at the start


cache = LRUCache(3)

data = [
    ('data-1', 1),
    ('data-2', 'abc'),
    ('data-3', [1, 2, 3]),
    ('data-4', True)
]

for k, v in data:
    cache.put(k, v)

# LRUCache({'data-4': True, 'data-3': [1, 2, 3], 'data-2': 'abc'})
print(cache)

d = cache.get('data-2')
# LRUCache({'data-2': 'abc', 'data-4': True, 'data-3': [1, 2, 3]})
print(cache)
