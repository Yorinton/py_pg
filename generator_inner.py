# def g():
#     for i in range(10):
#         yield i
#
# def c():
#     l = ['one', 'two', 'three', 'four', 'five']
#     for i in range(5):
#         yield '{}は英語で{}'.format(i+1,l[i])

g = (i for i in range(10) if i % 2 == 0)
l = ['one', 'two', 'three', 'four', 'five']
# tuple
c = tuple('{}は英語で{}'.format(i+1,l[i]) for i in range(5))
# generator
c2 = ('{}は英語で{}'.format(i+1,l[i]) for i in range(5))

print(type(g))
print(type(c))
print(type(c2))

print(c)
print(next(c2))
print(next(c2))
print(next(c2))