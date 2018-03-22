l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun', '']

def change_words(words, func):
    for word in words:
        # funcの定義に合わせてwordを変更
        print(func(word))


# def sample_func(word):
#     return word.capitalize()
#
# def sample_func2(word):
#     return word.lower()
# sample_func = lambda word: word.capitalize()


# l => change_wordsに渡す引数
# word => change_wordsに渡す関数の引数
# word.capitalize() => change_wordsに渡す関数で実行する処理
# change_words(l, lambda word: word.capitalize())
# change_words(l, lambda word: word.lower())


def list_slice(words, func):
    for word in words:
        print(func(word))

# lambdaは引数を操作して、操作された引数自体を返す場合に使えそう
list_slice(l, lambda word: word[0:1].capitalize())

days = [day.capitalize() for day in l if 'n' in day]
print(days)