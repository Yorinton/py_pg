r = [1,2,3,4,5,1,2,3]
print(r.index(3)) # 値からindexを調べる
print(r.index(2,3)) # 3番目以降の 2 のindexを調べる

print(r.count(3))

if 5 in r:
    print('exist')

    if 3 in r:
        print('exist')

r.sort() # ソート
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike'
# to_split = s.split(' ')
to_split_2 = s.split() # 引数がない場合空白でsplitする？
# print(to_split)
print(to_split_2)

x = '####'.join(to_split_2) # 指定した文字でlistの要素を結合する
print(x)

# print(help(list)) # listのマニュアル
