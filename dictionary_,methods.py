d = {'x':10, "y":20}

# key / value
k = d.keys()
print(type(k)) # <class 'dict_keys'>
v = d.values()
print(type(v)) # <class 'dict_values'>


# update
d2 = {'x':1000, 'j': 500}
d.update(d2) # 上書き + 追加
print(d.update(d2)) # {'x': 1000, 'y': 20, 'j': 500}

# 要素の取得
d.get('x')
type(d.get('z')) # <class 'NoneType'>

d.pop('x') # 取得 + 削除
del d['y'] # 削除
d.clear() # 中身を削除


d = {'a':100, 'b':200}
'a' in d # 中身の有無を確認 True
'j' in d # False
