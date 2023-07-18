

# ============================== START
"""

入力例1
1
koko 23 04/10 tokyo

出力例1
User{
nickname : koko
old : 23
birth : 04/10
state : tokyo
}

入力例2
3
mako 13 08/08 nara
megumi 14 11/02 saitama
taisei 16 12/04 nagano

出力例2
User{
nickname : mako
old : 13
birth : 08/08
state : nara
}
User{
nickname : megumi
old : 14
birth : 11/02
state : saitama
}
User{
nickname : taisei
old : 16
birth : 12/04
state : nagano
}

"""

# ===================== 構造体
N = int(input())


def Structure_01(loop_num):

    for _ in range(loop_num):
        n, o, b, s = input().split()
        print("User{")
        print("nickname : " + n)
        print("old : " + o)
        print("birth : " + b)
        print("state : " + s)
        print("}")


# ========= 実行
Structure_01(N)

# ========================================== END

# ========================================== START

"""

入力例1
1
koko 23 04/10 tokyo
23

出力例1
koko

入力例2
3
mako 13 08/08 nara
megumi 14 11/02 saitama
taisei 16 12/04 nagano
14

出力例2
megumi

"""


N_2 = int(input())

# ２次元配列で値取得 ================
arr_2 = []
for i in range(N_2):
    a, b, c, d = input().split()
    arr_2.append([a, int(b), c, d])

N_2_01 = int(input())

# ================== 答えの index の値　出力 ================
for j in range(N_2):
    if arr_2[j][1] == N_2_01:
        print(arr_2[j][0])

# ========================================== END

# ========================================== START
"""

入力例1
1
koko 23 04/10 tokyo

出力例1
koko 23 04/10 tokyo

入力例2
3
mako 13 08/08 nara
taisei 16 12/04 nagano
megumi 14 11/02 saitama

出力例2
mako 13 08/08 nara
megumi 14 11/02 saitama
taisei 16 12/04 nagano

"""

N_3 = int(input())
arr_3 = []

# ２次元配列で取得
for i in range(N_3):
    a, b, c, d = input().split()
    arr_3.append([a, int(b), c, d])

# ２次元ソート  [1] を key にして　ソート
arr_3 = sorted(arr_3, reverse=False, key=lambda x: x[1])

for j in range(N_3):
    for k in range(4):
        if(k != 3):
            print(str(arr_3[j][k]) + " ", end='')
        else:
            print(str(arr_3[j][k]))

# ========================================== END

# ========================================== START




# ========================================== END