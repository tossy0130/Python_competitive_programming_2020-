# ================================== Start

"""

入力例1
-10

出力例1
-9

入力例2
0

出力例2
1

"""

import collections
i_06 = int(input())


def B_06(num):
    print(num + 1)


# === 実行
B_06(i_06)

# ================================== End


# ================================== Start

"""
重複チェック

重複があった場合は true

重複がなかった場合は false
 
"""

arr_06 = ['HND', 'NRT', 'KIX', 'NGO', 'NGO']

s_06 = set(arr_06)
s_06_02 = set(arr_06)

if s_06 & s_06_02:
    print('true')  # 重複あり
else:
    print('false')  # 　重複なし

# ================================== End


# ================================== Start

"""
重複チェック

重複した値があったら、その個数を出力


"""

arr_07 = ["HND", "NRT", "KIX", "NGO", "NGO", "NGO", "NGO", "NGO"]

c_07 = collections.Counter(arr_07)

for k, v in c_07.items():
    if v > 1:
        print(v)


# ================================== End


# ================================== Start

"""
昇順　ソート


"""

arr_08 = [1, 3, 5, 6, 3, 2, 5, 23, 2]


def B_06_03(*args):
    arr_08.sort()
    for val in arr_08:
        print(val)


# === 実行
B_06_03(arr_08)


# ================================== End


# ================================== Start

"""

入力例1
4
S 1
F 2
E 5
Y 6

出力例1
1
2
5
6

入力例2
3
S -3
G -5
R -35

出力例2
-3
-5
-35

"""

b_09_i = int(input())


def B_08_04(b_09_i):
    arr_09 = []
    for i in range(b_09_i):
        # === key, value で取得する
        a, b = input().split()
        arr_09.append([a, int(b)])

    for val in range(b_09_i):
        print(arr_09[val][1])


# ====== 実行
B_08_04(b_09_i)


# ================================== End


# ================================== Start

"""

入力例1
8
90 777 8888 121 333 4 29 2

出力例1
2
4
29
90
121
333
777
8888

"""

num_09_i = int(input())


def B_06_05(num_09_i):
    arr_09 = []

    arr_09 = list(map(int, input().split()))
    arr_09.sort()
    for val in arr_09:
        print(str(val))


# === 実行 ===
B_06_05(num_09_i)


# ================================== End


# ================================== Start

"""

入力例1
7
A 1
D 6
C 2
G 4
B 70
A 10
B 5

出力例1
B 75
A 11
D 6
G 4
C 2

入力例2
3
G 0
S 3
E -2

出力例2
S 3
G 0
E -2

"""

num = int(input())
inputs = {}
result = {}

for i in range(num):
    tmp = input().split()

    exist = False
    for (key, value) in inputs.items():
        if key == tmp[0]:
            exist = True

    if exist:
        inputs[tmp[0]] = inputs[tmp[0]] + int(tmp[1])
    else:
        inputs[tmp[0]] = int(tmp[1])

# ソート用にkeyとvalueを反転させた辞書を作る
for (key, value) in inputs.items():
    result[value] = key

result = sorted(result.items(), reverse=True)

for i in result:
    print(i[1] + " " + str(i[0]))


# ================================== End


# ================================== Start


# ================================== End


# ================================== Start


# ================================== End
