# list型のコピー

################ 注意点 ##################
#                                       #
# 文字列や数値はデフォルトで値渡し           #
# listやdictionary等はデフォルトで参照渡し  #
#                                       #
#########################################


# 参照渡し
i = [1,2,3,4,5]
j = i # 参照渡し/ j も i と同じメモリのアドレスを見ている
j[0] = 100 # j の要素を変えると参照元が変わるので i も変わる
print('j =', j)
print('i =', i)

# コピー
x = [1,2,3,4,5]
y = x.copy() # 明示的にcopyを使った方が分かりやすい
# y = x[:]
y[0] = 100
print('y =', y)
print('x =', x)


# id
x = 20
y = x
y = 5
print(x)
print(y)
print(id(x))
print(id(y)) # x と y で異なるidが振られる

x = ['a', 'b']
y = x
y[0] = 'p'
print(x)
print(y)
print(id(x))
print(id(y)) # x と y で同じidが振られる