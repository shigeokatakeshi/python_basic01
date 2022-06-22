# 下記のコードが期待通り動作するような、1から6の整数をランダムに出力する dice() 関数を実装してください
# print(dice()) # 1から6の整数をランダムに出力する


import random

dice_m = [1, 2, 3, 4, 5, 6]


def dice():
    return random.choice(dice_m)


print(dice())