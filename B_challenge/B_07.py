# ================================== Start

"""

3つの文字列が3行で入力されるので、入力された文字列をそのまま1行ずつ出力してください。

"""

b_arr_07_01 = []


def B_07_01(num):
    for i in range(num):
        tmp = input()
        b_arr_07_01.append(tmp)

    for val in b_arr_07_01:
        print(val)


# === 実行
B_07_01(3)

# ================================== End


# ================================== Start

"""
入力例1
GINO

出力例1
G
H
I
J
K
L
M
N
O

"""

t_07 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z']


str_07_02 = input()


def B_07_02(num):
    str_a = num[0]
    str_b = num[-1]

    num_a = t_07.index(str_a)
    num_b = t_07.index(str_b)

    for i in range(num_a, num_b + 1):
        print(t_07[i])


# ============== B_07_02 実行
B_07_02(str_07_02)


# ================================== End


# ================================== Start


# ================================== End


# ================================== Start


# ================================== End


# ================================== Start


# ================================== End


# ================================== Start


# ================================== End


# ================================== Start


# ================================== End


# ================================== Start


# ================================== End


# ================================== Start


# ================================== End


# ================================== Start


# ================================== End
