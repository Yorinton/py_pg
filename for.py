# for

some_list = [1,2,3,4,5]

# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1
#


# some_listから要素を取り出して出力する
# phpで言うとforeach
for i in some_list:
    print(i)

for s in 'abcde':
    print(s)

for word in ['My', 'name', 'is', 'Mike']:
    if word == 'is':
        continue
    print(word)


# for else

for fruit in ['apple','banana','orange']:
    if fruit == 'banana':
        print('I hate banana')
        continue
    print('I ate ' + fruit)
else:
    print('I ate all')