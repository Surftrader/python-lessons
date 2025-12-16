from collections import deque

dq = deque()

dq = deque([1, 2, 3, 4, 5])
print(dq)  # deque([1, 2, 3, 4, 5])

dq = deque([1, 2, 3, 4, 5], maxlen=5)
print(dq[1])  # 2
print(dq[1])  # 2
# print(dq[10])  # IndexError: deque index out of range

dq[2] = 100
print(dq)  # deque([1, 2, 100, 4, 5], maxlen=5)

dq.append(6)
print(dq)  # deque([2, 100, 4, 5, 6], maxlen=5)

dq.appendleft(0)
print(dq)  # deque([0, 2, 100, 4, 5], maxlen=5)

dq = deque([1, 2, 3, 4, 5])
dq.appendleft(0)
print(dq)  # deque([0, 1, 2, 3, 4, 5])

dq.append(6)
print(dq)  # deque([0, 1, 2, 3, 4, 5, 6])

a = dq.pop()
print(a)  # 6
print(dq)  # deque([0, 1, 2, 3, 4, 5])

dq.popleft()
print(dq)  # deque([1, 2, 3, 4, 5])

try:
    dq = deque()
    right = dq.pop()
    left = dq.popleft()
    print(left, right)
    print(dq)
except IndexError as e:
    print(e)

dq = deque([1, 2, 3, 4, 5])
dq.extend('abc')
print(dq)  # deque([1, 2, 3, 4, 5, 'a', 'b', 'c'])

dq.extendleft('xyz')
print(dq)  # deque(['z', 'y', 'x', 1, 2, 3, 4, 5, 'a', 'b', 'c'])

dq.insert(1, 'hello')
print(dq)  # deque(['z', 'hello', 'y', 'x', 1, 2, 3, 4, 5, 'a', 'b', 'c'])

dq.insert(-1, 'hello')
# deque(['z', 'hello', 'y', 'x', 1, 2, 3, 4, 5, 'a', 'b', 'hello', 'c'])
print(dq)

dq.insert(100, 'hello')
# deque(['z', 'hello', 'y', 'x', 1, 2, 3, 4, 5, 'a', 'b', 'hello', 'c', 'hello'])
print(dq)

dq.insert(-100, 'hello')
# deque(['hello', 'z', 'hello', 'y', 'x', 1, 2, 3, 4, 5, 'a', 'b', 'hello', 'c', 'hello'])
print(dq)

dq = deque([1, 2, 3, 4, 3, 5])
print(dq)  # deque([1, 2, 3, 4, 3, 5])
dq.rotate()
print(dq)  # deque([5, 1, 2, 3, 4, 3])

dq.rotate(-2)
print(dq)  # deque([2, 3, 4, 3, 5, 1])

dq.rotate(3)
print(dq)  # deque([3, 5, 1, 2, 3, 4])

dq.remove(3)
print(dq)  # deque([5, 1, 2, 3, 4])

# dq.remove(100)  # ValueError: 100 is not in deque

dq.clear()
print(dq)  # deque([])

dq = deque([1, 2, 3, 4, 3, 5])
dq2 = dq.copy()
print(dq2)  # deque([1, 2, 3, 4, 3, 5])

dq2.append(100)
print(dq)   # deque([1, 2, 3, 4, 3, 5])
print(dq2)  # deque([1, 2, 3, 4, 3, 5, 100])
