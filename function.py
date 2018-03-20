# 関数

def say_something():
    s = 'hi'
    return s

print(type(say_something))

f = say_something
result = f() # () をつけることで実行になる
print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'pepper'
    else:
        return 'I don\'t know'

result = what_is_this('red')
print(result)


# pythonはタイプヒンティング効かない
def add_num(a: int, b: int) -> int:
    return a + b

r = add_num('a', 'b')
print(r)


# 位置引数とキーワード引数、デフォルト
def menu(entry='fish', drink='wine', dessert='ice'):
    print('entry = ', entry)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu(entry='beef', drink='ice', dessert='beer')

# キーワード引数の後に位置引数は指定出来ない
# menu(entry='chiken', 'juice', 'ice')


# リストを引数にする場合
# リストをデフォルト引数で渡すと、最初の１回だけ新しく定義される
# l に値を追加しても参照渡しなので、最初の l をずっと参照し続ける
# 空のリストはデフォルト引数に渡さない
def test_func(x, l = None):
    if l is None:
        # 関数の中だけ有効なリストを定義する
        l = []
    l.append(x)
    return l

y = [1,2,3]
r = test_func(100, y)
print(r)

y = [1,2,3]
r = test_func(200, y)
print(r)

r = test_func(100)
print(r)

r = test_func(200)
print(r)


# 位置引数のタプル化 *args
def say_something(word, *args): # 再度タプル化
    print(word)
    print(args)
    for arg in args:
        print(arg)

t = ('Mike', 'Nancy') # タプル

say_something('Hi', *t) # *t でアンパッキング

# キーワード引数による辞書化 **keyargs
def menu(**kwargs):
    # 辞書のvalueを取得するには.items()が必要
    for k, v in kwargs.items():
        print(k, v)

menu(entree='beef', drink='coffee')

d = {
    'entry': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}

menu(**d)

# * １つ => タプル / ** ２つ => 辞書

def menu(food, *args, **kwargs):
    print(food)
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg)

t = ('apple', 'orange') # タプル
d = {'entree':'beef', 'drink':'coffee'} # 辞書

menu('banana', *t, **d)