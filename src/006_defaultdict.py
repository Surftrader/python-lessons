from collections import defaultdict


# Usual dict
d = {'x': 0}
print(d['x'])  # 0
# print(d['y'])  # KeyError: 'y'
# d['count'] += 3  # KeyError: 'count'
d['count'] = 0
d['count'] += 3
print(list(d.keys()))  # ['x', 'count']
print(list(d.values()))  # [0, 3]
# for k, v in d.items():
#     print(k, v)


# Default dict
df = defaultdict(int)
print(df['x'])  # 0
print(df['y'])  # 0
print(df)  # defaultdict(<class 'int'>, {'x': 0, 'y': 0})
df['x'] = 5
print(df)  # defaultdict(<class 'int'>, {'x': 5, 'y': 0})
df['z'] = 7
print(df)  # defaultdict(<class 'int'>, {'x': 5, 'y': 0, 'z': 7})
df['z'] = 'abc'
print(df)  # defaultdict(<class 'int'>, {'x': 5, 'y': 0, 'z': 'abc'})
df['count'] += 3
# defaultdict(<class 'int'>, {'x': 5, 'y': 0, 'z': 'abc', 'count': 3})
print(df)


lst = ['Alex', 'Sergey', 'Fedor', 'Masha', 'Sergey', 'Fedor', 'Sergey']
df = defaultdict(int)
for x in lst:
    df[x] += 1
# defaultdict(<class 'int'>, {'Alex': 1, 'Sergey': 3, 'Fedor': 2, 'Masha': 1})
print(df)

df = defaultdict(list)
df['cities']
print(df)  # defaultdict(<class 'list'>, {'cities': []})
df['coords'].extend((1, 2, 3))
print(df)  # defaultdict(<class 'list'>, {'cities': [], 'coords': [1, 2, 3]})

d = defaultdict(bool, x=1, y=-5.2, descr='coords')
print(d)  # defaultdict(<class 'bool'>, {'x': 1, 'y': -5.2, 'descr': 'coords'})
print(d['fl'])  # False
# defaultdict(<class 'bool'>, {'x': 1, 'y': -5.2, 'descr': 'coords', 'fl': False})
print(d)

cities = [
    ('Alex', 'Kharkov'), ('Sergey', 'Kiev'), ('Masha', 'Uman'),
    ('Sergey', 'Kharkov'), ('Sergey', 'Kiev'), ('Masha', 'Zhitomir'),
    ('Alex', 'Uman'), ('Sergey', 'Kharkov'), ('Alex', 'Kharkov')
]

persons = defaultdict(set)
for k, v in cities:
    persons[k].add(v)

# defaultdict(<class 'set'>, {'Alex': {'Kharkov', 'Uman'}, 'Sergey': {'Kharkov', 'Kiev'}, 'Masha': {'Uman', 'Zhitomir'}})
print(persons)


def df_init():
    return 5


df = defaultdict(df_init)
# or -> df = defaultdict(lambda: 5)
x = df['x']
print(df)  # defaultdict(<function df_init at 0x10c5a9440>, {'x': 5})


def df_init_2(start=0):
    def counter():
        nonlocal start
        start += 1
        return start
    return counter


f = df_init_2()
print(f())  # 1
print(f())  # 2
print(f())  # 3


f = df_init_2(5)
print(f())  # 6
print(f())  # 7
print(f())  # 8

df = defaultdict(df_init_2(2))
x = df['x']
# defaultdict(<function df_init_2.<locals>.counter at 0x107b358a0>, {'x': 3})
print(df)
