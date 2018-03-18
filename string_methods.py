# 文字列メソッド
s = 'My name is Mike. Hi Mike.'
print(s)

is_start = s.startswith('x')
print(is_start)
is_start = s.startswith('My')
print(is_start)

print(s.find('Mike'))
print(s.rfind('Mike')) # 後ろから調べる（数え方は前から)
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))