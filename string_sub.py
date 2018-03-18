# 文字列代入

print('a is {}'.format('a'))
print('a is {2}{1}{0}'.format(1,2,3)) # 数値も型変換されて文字になる
print('My name is {first} {last}'.format(first='Yorihiro', last='Katsuki'))

#型変換
x = str(1)
y = str(True)
print(x)
print(y)