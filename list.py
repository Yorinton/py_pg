# リスト型

print(list('abceefg'))

n = [1,2,3,4,5,6,7,8,9,10]
print(n[::2]) # 一つ飛ばし
print(n[::-1]) # 逆から

a = ['a', 'b', 'c']
n = [1,2,3]
x = [a,n]

s = ['a','b','c','d','e','f','g']
s[0] = 'X'
s[2:5] = ['C','D','E']
s[2:5] = []
print(s)


n = [1,2,3,4,5,6,7,8,9,10]
n.append(100) # 要素を最後に追加
n.insert(0,200) # 要素を指定した場所に挿入
n.pop() # 最後の要素を取り出す
print(n.pop(0)) # 指定した場所の要素を取り出す
print(n)

del n[0] #削除
del n # n自体削除(変数自体削除するので定義されていないことになる)

n = [1,2,2,2,3]
n.remove(2) # 2を削除する
n.remove(2)
n.remove(2)
# n.remove(2) # 消せる2が無い、と怒られる

x = [1,2,3,4,5]
y = [6,7,8,9,10]
x.extend(y)
print(x)


# リスト内包表記
l = ['aaa', ' bbb', 'ccc\nccc', ' ', '', '  ddd  ']
for p in l:
    # if(p.strip()):
    #     print('strip出来る', p.strip())
    # else:
    #     print('strip出来ない', p.strip(),p)
    print(p.strip())

# new_lists = [p.strip() for p in l if p.strip()]
# print(new_lists)

l = ['##' + x.strip() + '##' for x in l if x.strip()]
print(l)

l = [0] * 0
print(l)

