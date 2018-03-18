y = {1,2,3}
x = 10

if x in y:
    print('in')

if x not in y:
    print('not in')


# 数値同士を比較する時はあまりnotは使わない
a = 1
b = 2

# if not a == b:
#     print('Not equal')

if a != b:
    print('Not equal')


# boolean型の時は not を使う
is_ok = False

if is_ok:
    print('hello')
elif not is_ok:
    print('good bye')