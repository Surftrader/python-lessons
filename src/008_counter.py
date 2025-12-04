from collections import Counter


s = 'abrakadabra'
syms = Counter(s)
print(syms)  # Counter({'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1})

c1 = Counter(['abc', 'cba', 'abc', 'ABC', 'ABC'])
c2 = Counter((1, 2, 0, 4, 3, 2, 1, 1))
c3 = Counter([(1, 2, 3), ('a', 'b'), (1, 2), (1, 2, 3)])

print(c1)  # Counter({'abc': 2, 'ABC': 2, 'cba': 1})
print(c2)  # Counter({1: 3, 2: 2, 0: 1, 4: 1, 3: 1})
print(c3)  # Counter({(1, 2, 3): 2, ('a', 'b'): 1, (1, 2): 1})

# c4 = Counter([[1, 2, 3], ('a', 'b'), (1, 2), (1, 2, 3)])
# print(c4)  # TypeError: unhashable type: 'list'

c5 = Counter({'Alex': 2, 'Mike': 1})
print(c5)  # Counter({'Alex': 2, 'Mike': 1})
print(c5['Alex'])  # 2
print(c5['Sergey'])  # 0

c6 = Counter(car=1, house=2, dog=5)
print(c6)  # Counter({'dog': 5, 'house': 2, 'car': 1})

c5.update({'Alex': 1, 'Serg': 5})
print(c5)  # Counter({'Serg': 5, 'Alex': 3, 'Mike': 1})
print(c5.most_common(2))  # [('Serg', 5), ('Alex', 3)]
print(c5.most_common())  # [('Serg', 5), ('Alex', 3), ('Mike', 1)]

print(c5.elements())  # <itertools.chain object at 0x10c373100>
# ['Alex', 'Alex', 'Alex', 'Mike', 'Serg', 'Serg', 'Serg', 'Serg', 'Serg']
print(list(c5.elements()))
print(c5.total())  # 9

c1 = Counter(a=1, b=3, c=2)
c2 = Counter(b=2, d=3, f=1)
print(c1 + c2)  # Counter({'b': 5, 'd': 3, 'c': 2, 'a': 1, 'f': 1})
print(c1 - c2)  # Counter({'c': 2, 'a': 1, 'b': 1})
print(c2 - c1)  # Counter({'d': 3, 'f': 1})
print(c1 | c2)  # Counter({'b': 3, 'd': 3, 'c': 2, 'a': 1, 'f': 1})
print(c1 & c2)  # Counter({'b': 2})
c1 -= c2
print(c1)  # Counter({'c': 2, 'a': 1, 'b': 1})
c2 += c1
print(c2)  # Counter({'b': 3, 'd': 3, 'c': 2, 'f': 1, 'a': 1})
c1 |= c2
print(c1)  # Counter({'b': 3, 'd': 3, 'c': 2, 'a': 1, 'f': 1})
c1 &= c2
print(c1)  # Counter({'b': 3, 'd': 3, 'c': 2, 'a': 1, 'f': 1})

c1 = Counter(a=1, b=3, c=2)
c2 = Counter(b=2, d=3, f=1)

print(c1 - c2)  # Counter({'c': 2, 'a': 1, 'b': 1})
c1.subtract(c2)
print(c1)  # Counter({'c': 2, 'a': 1, 'b': 1, 'f': -1, 'd': -3})
