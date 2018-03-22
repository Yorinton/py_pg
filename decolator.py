def print_more(func):
    def wrapper(*args, **kwargs):
        print('func', func.__name__)
        print('args', args)
        print('kwargs', kwargs)
        result = func(*args, **kwargs)
        print('result', result)
        return result
    return wrapper


def print_info(func):
    def wrapper(*args, **kwargs):
        print('start') # f(10, 20)が実行された時点で表示される
        result = func(*args, **kwargs) # f(10, 20)が実行された時点では変数に格納されるだけ
        print('end') # f(10, 20)が実行された時点で表示される
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20) # add_numのwrapperが返る
# r = f(10, 20) # wrapperの引数に10, 20を与える
print(r) # resultに格納された add_num(10, 20)の結果が表示される

@print_info
def sub_num(a, b):
    return a - b

r = sub_num(100, 15)
print(r)



# print('start')
# r = add_num(10, 20)
# print('end')
#
# print(r)