# リスト内包表記

t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

r = []
for i in t:
    r.append(i)

print(r)

# appendしない & メモリを使わないので早い
r2 = [i for i in t if i % 2 == 1]

print(r2)

r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

# for文一つやifがつく時に使う
# あまり長いリスト内包表記は分かりづらい
r = [i*j for i in t for j in t2]

print(r)