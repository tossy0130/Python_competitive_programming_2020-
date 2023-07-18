# ================================== Start

"""
入力例1
3
0
7
5

出力例1
3
0
7
5

入力例2
3
8
0
9

出力例2
3
8
0
9

"""
num = int(input())


def Stack_Q_01(num):
    # スタック
    i = 0
    arr_1 = []
    while num > i:
        tmp = int(input())
        arr_1.append(tmp)
        i = i + 1

    # キュー
    print(num)
    for j in arr_1:
        print(j)


# === 実行
Stack_Q_01(num)

# ================================== END

# ================================== Start

""" 

入力される値
Q
query_1
query_2
...
query_Q

入力例1
4
2
1 6
1 5
1 9

出力例1
3
6
5
9

入力例2
2
2
2

出力例2
0

"""

num_02 = int(input())


def Stack_Q_02(num_02):

    arr_02 = []
    for i in range(num_02):
        # === 配列に分ける
        q = input().split()
        if q[0] == '1':
            arr_02.append(q[1])
        else:
            continue

    print(len(arr_02))

    for q_val in arr_02:
        print(q_val)


# === 関数　実行
Stack_Q_02(num_02)

# ================================== End
