# 集合型


a = {1,2,3,3,4,4,4,5,6}
b = {2,3,3,5,6,6,7}
print(a) # {1, 2, 3, 4, 5, 6} 重複が取り除かれる

print(a - b) # {1, 4}
print(b - a) # {7} あるものだけ引く

print(a & b) # a にも bにもあるもの
print(a | b) # a か bにあるもの
print(a ^ b) # a か bにあるものの中で重複していないもの


# 集合型のメソッド

# 集合には順番がない
s = {1,2,3,4,54}
s.add(6) # {1, 2, 3, 4, 6, 54}
s.remove(6) # {1, 2, 3, 4, 54}
s.clear() # set() (空のset型)

s = {'a','aa','こんにちわ','また明日'}


# 集合の使い所
# 共通の友達を見つける時など

my_friends = {'A', 'B', 'C'}
A_friends = {'B','D','E','F'}


all_friends = my_friends.union(A_friends)
print('みんな友達',all_friends)
print(my_friends & A_friends) # 共通の項目 {B}

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f) # set型に変換 ユニークなものだけ取得
print(kind)

