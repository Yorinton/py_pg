# タプル型
# 編集ではなく、読み込み専用

t = (1,2,3,4,1,2)

t = ([1,2,3], [4,5,6])
# t[0] = [1] # エラーになる
t[0][0] = 100 # これは出来る

type(t)

t = (1) # int
type(t)
t = ('test') # string
type(t)

# tuple同士の計算は出来る
new_tuple = (1,2,3,) + (4,5,6)
print(new_tuple)


# new_tuple = (1) + (4,5,6) # int + tupleは不可
new_tuple = (1,) + (4,5,6) # これはOK



# tupleのアンパッキング
num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = 10, 20
print(x, y)

print(type(y))

min, max = 0, 100
print(min, max)


# 読みづらいので各々定義する
a, b, c, d, e, f = 'Mike', '1', 'aa', 'obao', 'obaa', 'ffff'

# 変数の値の入れ替え
i = 10
j = 20
tmp = i
i = j
j = tmp

print(i, j)

# 簡単に出来る変数の入れ替え
a, b = 100, 200
print(a, b)
a,b = b, a
print(a, b)










