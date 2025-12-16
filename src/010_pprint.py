import pprint

d_end = {'tree': ['дерево'], 'car': ['машина', 'авто'], 'leaf': [
    'ліст'], 'river': ['річка'], 'go': ['йти', 'їхати', 'їздити'], 'milk': ['молоко']}

print(d_end)
pprint.pprint(d_end)

dp = {'coords': (100, 200, 300, 400, 500, 600, 700, 1024),
      'matrix': [(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 6), (-1, -2, -3, -4, -5, -6)],
      'x': 6.54,
      'y': 10.23,
      (10, 20): 'coords of the point'}

pprint.pprint(dp)
pprint.pprint(dp, indent=5)
pprint.pprint(dp, indent=5, width=40)
pprint.pprint(dp, depth=2)

s = pprint.pformat(dp)
print(s)

s = pprint.pformat(dp, indent=4, width=40, depth=2)
print(s)

pr = pprint.PrettyPrinter(indent=2, width=70, depth=3, compact=True)
pr.pprint(dp)
