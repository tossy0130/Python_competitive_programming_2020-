# ================================== Start

"""

文字列が入力されるので、その長さを出力

入力例1
input

出力例1
5

入力例2
abc123

"""

num_01 = input()


def B_challenge_01(num_01):
    print(len(num_01))


# === 実行
B_challenge_01(num_01)

# ================================== End

# ================================== Start

"""

文字列が入力されるので、1文字目を出力

入力例1
input

出力例1
i

入力例2
abc123

出力例2
a

"""

num_02 = input()


def B_challenge_02(num_02):
    print(num_02[:1])


# === 実行
B_challenge_02(num_02)


# ================================== End

# ================================== Start

"""

指定された配列（リスト）を定義し、配列（リスト）の要素をインデックス順に１行ずつ出力

"""

arr_03 = ['Nara', 'Shiga', 'Hokkaido', 'Chiba']


def B_challenge_03(arr_03):
    for val in arr_03:
        print(val)


# === 実行
B_challenge_03(arr_03)

# ================================== End

# ================================== Start

"""

文字列が入力されるので、それらの文字を、1文字ずつ出力

入力例1
input

出力例1
i
n
p
u
t

"""

arr_04 = list(input())


def B_challenge_04(arr_04):
    for val in arr_04:
        print(val)


# === 実行
B_challenge_04(arr_04)

# ================================== End

# ================================== Start

"""

1行目の文字が、2行目の文字列の中に何個出現するかをカウントして出力

入力例1
A
abdeeAAbAAAbfde

出力例1
5

"""

num_05 = input()
arr_05 = list(input())


def B_challenge_05(num_05, arr_05):
    ans = 0
    for val in arr_05:
        if num_05 == val:
            ans = ans + 1
    return ans


# === 実行
a_05 = B_challenge_05(num_05, arr_05)
print(a_05)


# ================================== End

# ================================== Start

"""

文字列が入力されるので、その長さを出力

入力例1
input

出力例1
5

"""

num_06 = input()


def B_challenge_06(num_06):
    print(len(num_06))


B_challenge_06(num_06)


# ================================== End

# ================================== Start

"""

文字列が入力されるので、1文字目を出力

入力例1
read

出力例1
r

"""

num_07 = list(input())


def B_challenge_07(num_07):
    print(num_07[0])


# === 実行
B_challenge_07(num_07)


# ================================== End

# ================================== Start

"""

文字列が入力されるので、それらの文字を、1文字ずつ出力

入力例1
read

出力例1
r
e
a
d

"""

num_08 = list(input())


def B_challenge_08(num_08):
    for val in num_08:
        print(val)


# === 実行
B_challenge_08(num_08)


# ================================== End

# ================================== Start

"""
文字列 s が入力されるので、1文字目と2文字目を出力

入力例1
read

出力例1
r e

入力例2
scale

出力例2
s c

"""

arr_09 = list(input())


def B_challenge_09(arr_09):
    print(arr_09[0] + ' ' + arr_09[1])


# === 実行
B_challenge_09(arr_09)

# ================================== End

# ================================== Start

"""
=========== ANS ============

文字列 s が入力されるので、n 文字目と n + 1 文字目を出力してください。 n + 1 文字目がない場合は何も出力しない

入力例1
2
read

出力例1
e a

"""
n = int(input()) - 1
string = input()

if n + 1 < len(string):
    print(string[n] + " " + string[n + 1])

# ================================== End

# ================================== Start

"""
1行目で文字列 s、2行目で文字列 t が入力されます。
s が t の中で何回出現するかカウントして出力

入力例1
AA
abdeeAAbAAAbfde

出力例1
3

入力例2
el
scale

出力例2
0

"""


# ===================== ANS

pattern = input()
string = input()
result = 0

for i in range(len(string) - len(pattern) + 1):
    portion = string[i: i + len(pattern)]

    if portion == pattern:
        result += 1

print(result)


# ===================== ANS END


t_list_11 = input()
s_lsit_11 = input()

ans = 0

for i in range(len(s_lsit_11) - len(t_list_11) + 1):
    pos = s_lsit_11[i: i + len(t_list_11)]

    if t_list_11 == pos:
        ans += 1

print(ans)


# ================================== End

# ================================== Start

"""

"""

# ================================== End

# ================================== Start

"""

"""

# ================================== End

# ================================== Start

"""

"""

# ================================== End
