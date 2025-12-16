from collections import ChainMap


d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
ch = ChainMap(d1, d2)
print(ch)  # ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})

print(ch['a'])  # 1
print(ch['b'])  # 2
print(ch['c'])  # 4

ch2 = ChainMap(d2, d1)
print(ch2)  # ChainMap({'b': 3, 'c': 4}, {'a': 1, 'b': 2})

print(ch2['a'])  # 1
print(ch2['b'])  # 3
print(ch2['c'])  # 4

print(ch)  # ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
d1['a'] = 5
print(ch)  # ChainMap({'a': 5, 'b': 2}, {'b': 3, 'c': 4})
ch['c'] = -1
print(ch)  # ChainMap({'a': 5, 'b': 2, 'c': -1}, {'b': 3, 'c': 4})

ch_new = ch.new_child({'a': 100, 'd': 7, 'key': [1, 2, 3]})
# ChainMap({'a': 100, 'd': 7, 'key': [1, 2, 3]}, {'a': 5, 'b': 2, 'c': -1}, {'b': 3, 'c': 4})
print(ch_new)
print(ch_new['a'])  # 100
print(ch)  # ChainMap({'a': 5, 'b': 2, 'c': -1}, {'b': 3, 'c': 4})

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
ch = ChainMap(d1, d2)
print(ch)  # ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})

print(ch.maps)  # [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]
ch.maps.reverse()
print(ch.maps)  # [{'b': 3, 'c': 4}, {'a': 1, 'b': 2}]
print(ch)  # ChainMap({'b': 3, 'c': 4}, {'a': 1, 'b': 2})
print(ch['b'])  # 3

d2['b'] = -1
print(ch)  # ChainMap({'b': -1, 'c': 4}, {'a': 1, 'b': 2})
