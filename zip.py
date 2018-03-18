days = ['Mon', 'Tue', 'wed']
fruits = ['apple','banana','orange']
drinks = ['coffie','tea','beer']

# for i in range(3):
#     print(days[i],fruits[i],drinks[i])

# zip関数 複数のリストを一緒にforで処理したい時に便利
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)