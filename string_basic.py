# 文字列基本
s = 'test'

print(s)
print("hello")
print("I don't know")
print("say \"I don't know\"")

print("hello, \nhow are you?")

print('C:\\name\\name')
print(r'C:\name\name')

# 改行を入れてくれる
print("############")
print("""
line1
line2
line3
line4
""")
print("############")


print("############")
print("""\
line1
line2
line3
line4\
""")
print("############")


print('Hi, ' * 3 + 'Mike')

print('Py' + 'thon')
pre = 'Py'
print(pre + 'thon')

s = ('aaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbb')

print(s)

s = 'aaaaaaaaaaaaaaaaaaa'\
    'bbbbbbbbbbbbbbbbbbb'

print(s)

word = 'python'
print(word[0],word[1],word[-1],sep='\n')
print(word[0:2])
print("#######")
print(word[2:5]) #5番目の文字は入らない
print("#######")
print(word[:5])
print(word[2:])
word = 'j' + word[1:]
print(word)

print(word[:]) # コピー
n = len(word)
print(n)