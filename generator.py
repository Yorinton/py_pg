l = ['Good Morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)


print('##########')

def greeting():
    # これらの要素をgenerateしていく
    yield 'Good morning'
    # 重たい処理が間に入った時に小分けに実行出来る
    for i in range(5):
        print(i)
    yield 'Good afternoon'
    for i in range(5):
        print(i)
    yield 'Good night'

def counter(num=10):
    for _ in range(num):
        yield 'run'

# for g in greeting():
#     print(g)

g = greeting() # generator生成
c = counter() # generator生成

print(next(g))
# for文と違って間に自由に処理を挟める
print(next(c))
print(next(g))
print(next(g))

