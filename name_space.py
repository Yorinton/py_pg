"""
Test Test ########
"""

animal = 'cat'

def func():
    """###Test func doc###"""
    animal = 'dog'
    print(func.__name__)
    print(func.__doc__)
    print(locals())
    # global animal
    # print('local:',locals())

func()
print('global:', globals())
# print('global:',globals())
