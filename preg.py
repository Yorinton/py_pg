import re

# m = re.search('^\(?（?\d+\.?．?）?\)?', '第４条')
#
# t = '|'.join(['a','b'])
#
# print(t)
# print(m)
# print(m.group())


NUMBER_REGEX = ['\d+']
JP_NUMBER_WORDS = ['一', '二', '三', '四', '五', '六', '七', '八', '九つ', '十', '壱', '弐', '参']
JP_ALPHABET = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス',
               'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ',
               'ヒ', 'フ', 'ヘ', 'ホ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン']

NUMBER_CIRCLE = ['①','②','③','④','⑤','⑥','⑦','⑧','⑨']
NUMBER_PARENTHESIS = ['⑴', '⑵', '⑶', '⑷', '⑸', '⑹']
NUMBER_LATIN = ['(x)', '(ix)', '(viii)', '(vii)', '(vi)', '(iv)', '(iii)', '(ii)', '(i)']
#NUMBER_LATIN1 = ['ⅰ）', 'ⅱ）', 'ⅲ）', 'ⅳ）', 'ⅴ）']
NUMBER_LATIN1 = ['ⅴ）', 'ⅳ）', 'ⅲ）', 'ⅱ）', 'ⅰ）']
NUMBER_LATIN2 = ['（x）', '（ix）', '（viii）', '（vii）', '（vi）', '（iv）', '（iii）', '（ii）', '（i）']
NUMBER_LATIN3 = ['ⅴ)', 'ⅳ)', 'ⅲ)', 'ⅱ)', 'ⅰ)']

TERM_PATTERN = '|'.join(['^第\s*{}\s*条'.format(num_char) for num_char in NUMBER_REGEX + JP_NUMBER_WORDS])
LABEL_PATTERN = r'^[【(（]+.+?[）)】]+\s*'
TITLE_PATTERN = r'[【(（]+.+?[）)】]+\s*'

NUMBER_BULLET_PATTERN = '|'.join(['^\(?（?'+x+'\.?．?）?\)?'
    for x in JP_NUMBER_WORDS+JP_ALPHABET+NUMBER_CIRCLE+NUMBER_LATIN+NUMBER_LATIN1+NUMBER_PARENTHESIS+NUMBER_REGEX
])

m = re.search(NUMBER_BULLET_PATTERN,'(2) 甲は、前項の手数料を、当月の甲の加盟店手数料の入金後 5 営業日以内に、乙の指定する口座に振')
if m:
    bullet = m.group()
    bullet = bullet.replace('（', '(').replace('）', ')')
    bullet = bullet.replace('．', '.')
    print(bullet)
    print('NUMBER_BULLETマッチ')

else:
    print('NUMBER_BULLETマッチせず')

m = re.search(TERM_PATTERN, '第３条(手数料など)')
if m:
    print('TERMマッチ')
else:
    print('TERMマッチせず')

m = re.search(TITLE_PATTERN, '第４条(手数料等)')
if m:
    print('TITLEマッチ')
else:
    print('TITLEマッチせず')

m = re.search(LABEL_PATTERN, '第４条(手数料等)')
if m:
    print('LABELマッチ')
else:
    print('LABELマッチせず')


m = re.search(NUMBER_BULLET_PATTERN, '1．本契約にいう「秘密情報」とは、甲及び乙が、本契約上の義務の履行に関して相互に開示し、受領又は知得したすべての情報をいう。')
if m:
    print('マッチ')
else:
    print('マッチせず')

content = '第４条(手数料等)'

if content[-1] in ['）', ')'] or len(content) < 20:
    print('ラベルだよ')
else:
    print('ラベルじゃないよ')

# for collection in [JP_NUMBER_WORDS, JP_ALPHABET, NUMBER_CIRCLE, NUMBER_LATIN, NUMBER_LATIN1, NUMBER_LATIN2,
#                    NUMBER_LATIN3, NUMBER_PARENTHESIS]:
#     # if self.bullet_value in collection:
#     #    return collection[0]
#
#     # c = '①'とか'(1)'とか※全角（）はこの時点で()になっている
#     for c in collection:
#         # self.ballet_valueの中に、①,(1),カタカナ,五,ⅳ）,（x）,数値etcの値が存在する場合、
#         # そのマッチした文字を返す。無ければ次のループへ。
#         # 最初にマッチしたものが返ってくる
#         print(c)
#         if c in '(2)':
#             # 何故[0]なのか？
#             print('アウトプット',collection[0])


# number_value = re.sub('\d+', 'X', '1.')
# print(number_value)

print(list(range(len(NUMBER_CIRCLE))))

l = [9,2,3,4,10,0,1,3]
print(min(l))
print('len',len(l))

print([0] + [1,3])

level_order = [0,0,1,1]
min_level = min(level_order)
idxs = [idx for idx, v in enumerate(level_order) if v == min_level]
print(idxs) # [0,1]
if 0 not in idxs:
    idxs = [0] + idxs
if len(level_order) not in idxs:
    idxs = idxs + [len(level_order)]
print(idxs)
