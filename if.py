# if / 論理演算子

# if
x = 10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('ten')
else:
    print('positive')


a = 5
b = -10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')
    elif b <= 0:
        print('b is negative or zero')


# 論理演算子

a = 1
b = 1

# a と bが等しい
print(a == b)

# a と bが異なる
a != b

a < b

a > b

a <= b

a >= b

a > 0 and b > 0

a > 0 or b > 0

print(a > 0 and b > 0)

if a > 0 or b > 0:
    print('a or b is positive')

# 再掲 set型同士の比較
a = {1,2,3,4}
b = {4,5,6,7}

print(a & b) # a にも bにもあるもの
print(a | b) # a か bにあるもの
print(a ^ b) # a か bにあるものの中で重複していないもの


# 値判定のテクニック

# is_ok = True
is_ok = 100 # trueと判定される
is_ok = -10 # これもtrue
is_ok = 'test' #これもtrue
is_ok = '' # これはfalse
is_ok = [] # これもfalse
is_ok = [1,2,3] # これはtrue
is_ok = None # これはfalse
# 中身がないもの,Noneは全てfalseと判定される


if is_ok:
    print('OK')
else:
    print('No')

# Noneオブジェクトの判定
is_empty = None

# is_emptyがNoneなら実行
if is_empty is None:
    print('None!!')

if is_empty is not None:
    print('None!!')

# == は 値 を比較
print(1 == True)
# isは オブジェクト(型) を比較する
print(1 is True) # falseになる
