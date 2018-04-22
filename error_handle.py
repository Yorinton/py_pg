l = [1,2,3]
i = 5

try:
    print(l[i])
except IndexError as ex:
    print("Don't worry:{}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other: {}'.format(ex))
else: # exceptionをキャッチしなかった時だけ実行
    print('done')
finally: # 必ず実行する文
    print('clean up')
