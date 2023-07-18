
# ================================== Start

"""

出力例1
Hello
World

入力例2
0 1

出力例2
0
1

入力例3
a b

出力例3
a
b

"""
str_01 = input()

for str_01_val in str_01.split():
    print(str_01_val)

# ================================== End

# ================================== Start

""" 
スペース区切りの2つの整数が入力されるので、それらを足して出力

入力例1
0 0

出力例1
0

入力例2
1 2

出力例2
3

入力例3
10 20

出力例3
30

"""

a_02, b_02 = map(int, input().split())
print(a_02 + b_02)

# ================================== End

# ================================== Start

"""

"""

str_input_03 = input()

print(len(str_input_03))

# ================================== End

# ================================== Start

"""
文字列が入力されるので、1文字目を出力

入力例1
abc

出力例1
a

入力例2
123

出力例2
1

"""

str_in_04 = input()
print(str_in_04[:1])

# ================================== End

# ================================== Start

"""

入力例1
0 10

出力例1
0
1
2
3
4
5
6
7
8
9
10

"""

num_05a, num_05b = map(int, input().split())

i = num_05a
while i <= num_05b:
    print(i)
    i = i + 1


# ================================== End

# ================================== Start

"""

入力例1
2 6
this is a pen

出力例1
his i

"""

num_06a, num_06b = map(int, input().split())

str_06 = input()

print(str_06[num_06a:num_06b])


# ================================== End

# ================================== Start

"""

入力例1
2 6
this is a pen

出力例1
his i

入力例2
2 6
Welcome to the paiza! I`m studying ruby!

出力例2
elcom

"""

num_06a, num_06b = map(int, input().split())
str_06 = input()

print(str_06[num_06a - 1:num_06b])


# ================================== End

# ================================== Start

"""

入力例1
Hello World

出力例1
Hello
World

入力例2
0 1

出力例2
0
1

"""

str_07 = input()

for val in str_07.split():
    print(val)

# ================================== End

# ================================== Start

"""

入力例1
a

出力例1
A

入力例2
m

出力例2
M

"""

str_08 = input()
print(str_08.upper())

# ================================== End


# ================================== Start

"""

スペース区切りの2つの整数と、文字列が入力されます。2つの整数の範囲の部分文字列を、大文字にして出力

入力例1
2 6
this is a pen

出力例1
tHIS Is a pen

入力例2
2 6
Welcome to the paiza! I`m studying ruby!

出力例2
WELCOMe to the paiza! I`m studying ruby!

"""


num_8a, num8_b = map(int, input().split())
str_08 = input()


def B_challenge_08(num_8a, num8_b, str_08):

    # === 大文字に入れ替え
    tmp = str_08[num_8a - 1:num8_b].upper()
    ans_08 = str_08.replace(str_08[num_8a - 1:num8_b], tmp)
    print(ans_08)


# === 実行
B_challenge_08(num_8a, num8_b, str_08)

# ================================== End
