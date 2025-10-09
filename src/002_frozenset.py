
def main():
    fs = frozenset([1, 2, 3, 2, 3])
    print(fs)  # frozenset({1, 2, 3})

    t = ('a', 'b', True, 10, 'b')
    fs = frozenset(t)
    print(fs)  # frozenset({'b', True, 10, 'a'})

    # lst = [1, [2, 4], {6, 5, 5}]
    # fs = frozenset(lst)  # TypeError: unhashable type: 'list'

    s = {'abc', 10, -5.3, True}
    f = frozenset(['a', 'b', 'c', 10, False])
    # frozenset({False, True, 'b', 'c', 10, 'a', -5.3, 'abc'})
    print(f.union(s))
    # frozenset({False, True, 'b', 'c', 10, 'a', -5.3, 'abc'})
    print(f | s)
    print(f.intersection(s))  # frozenset({10})
    print(f & s)  # frozenset({10})
    print(s & f)  # {10}
    print(f.difference(s))  # frozenset({False, 'c', 'b', 'a'})
    print(f - s)  # frozenset({False, 'c', 'b', 'a'})
    print(s - f)  # {'abc', True, -5.3}
    # frozenset({False, True, 'abc', 'a', 'c', -5.3, 'b'})
    print(f.symmetric_difference(s))
    print(f ^ s)  # frozenset({False, True, 'abc', 'a', 'c', -5.3, 'b'})
    print(s ^ f)  # {False, 'b', True, 'a', 'abc', 'c', -5.3}

    s = {1, 2, 3}
    f = frozenset([1, 2, 3, 4])
    print(s == f)  # False
    print(s < f)  # True

    s = {1, 2}
    f = frozenset([1, 2])
    d_1 = {f: 'frozenset'}
    print(d_1)  # {frozenset({1, 2}): 'frozenset'}
    # d_2 = {s: 'set'}  # TypeError: unhashable type: 'set'
    d_2 = {frozenset(s): 'set'}
    print(d_2)  # {frozenset({1, 2}): 'set'}
    d_2 = {(d_2_key := frozenset(s)): 'set'}
    print(d_2_key)  # frozenset({1, 2})


if __name__ == '__main__':
    main()
