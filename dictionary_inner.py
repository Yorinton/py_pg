# 辞書包括表記

w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
# zip関数はそれぞれ引数のリストを対応する変数に展開する
for x,y in zip(w,f):
    d[x] = y

print(d)

# キー: バリュー for ・・の形
d = {x: y for x, y in zip(w,f)}

print(d)

# リスト内包表記(参照)
# r2 = [i for i in t if i % 2 == 1]
l = [x for x in zip(w,f)]
print(l)