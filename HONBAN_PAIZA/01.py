"""

############# ステータス 失敗

入力例1
6
le 120.3
ge 115.7
le 122.0
ge 116.9
le 119.1
le 117.6
出力例1
116.9 117.6

"""

num = int(input())

dmg_A = {}

# 辞書型で取得
for i in range(num):
    [a, b] = input().split()
    b = float(b)
    dmg_A[a] = b

print(str(dmg_A["ge"]) + ' ' + str(dmg_A["le"]))