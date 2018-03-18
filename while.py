# while文

# count = 0
#
# while count < 5:
#     print(count)
#     count += 1

# break文でwhileを抜ける
# continueは後の処理をスキップして次のループに行く

# count = 0
# while True:
#     if count >=5:
#         break
#
#     if count == 2:
#         count += 1
#         continue
#
#     print(count)
#     count += 1


# while else文
# whileのループ終了後elseの中の処理を実行

count = 0
while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
else:
    print('done')