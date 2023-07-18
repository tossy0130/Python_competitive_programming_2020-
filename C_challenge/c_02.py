# ================================== Start

"""

入力例1
2
Kirishima 1
Kyoko 2
Kirishima

出力例1
1

"""

"""

＊＊＊　模範　＊＊＊

n = int(input())
zaisan = {}

for i in range(n):
    [s, a] = input().split()
    zaisan[s] = a

S = input()

print(zaisan[S])

"""

num = int(input())

arr_01 = []
for i in range(num):
    a, b = input().split()
    arr_01.append([a, int(b)])

t_str = input()

# === ２次元配列で比較
for j in range(num):
    if arr_01[j][0] == t_str:
        print(arr_01[j][1])


# ================================== End


# ================================== Start

"""

入力例1
2
Kirishima
Kyoko
2
Kyoko 1
Kyoko 2
Kyoko

出力例1
3

入力例2
3
paiiza
paiza
paiiiza
2
paiiza 2
paiiiza 3
paiza

出力例2
0

"""

# ================================== End


# ================================== Start

"""

入力例1
2
Kirishima
Kyoko
2
Kyoko 1
Kyoko 2
Kyoko

出力例1
3

入力例2
3
paiiza
paiza
paiiiza
2
paiiza 2
paiiiza 3
paiza

出力例2
0


＊＊＊＊＊＊　お手本　＊＊＊＊＊＊

n = int(input())
dmg = {}

for i in range(n):
    s = input()
    dmg[s] = 0

m = int(input())

for i in range(m):
    [p, a] = input().split()
    a = int(a)
    dmg[p] += a

S = input()

print(dmg[S])


"""


num_02 = int(input())

arr_02 = []

tmp_num = 0

# === ２次元配列で取得
for i in range(num_02):
    tmp = input()
    arr_02.append([tmp, int(tmp_num)])

arr_02_02 = []

# === ２次元配列で取得
num_02_02 = int(input())
for j in range(num_02_02):
    a, b = input().split()
    arr_02_02.append([a, int(b)])

str_02 = input()  # 比較文字を取得

sum_num_02 = 0  # 合計出力用
no_sum_02 = 0  # 比較文字がなかった場合の用 「０」定数
to_02_flg = True  # 比較文字があるか、ないかの判別フラグ

# === 比較リストにあった場合は、「加算」　、　無い場合は「０」
for i in range(num_02_02):
    if arr_02_02[i][0] == str_02:
        sum_num_02 += arr_02_02[i][1]
        to_02_flg = True
    else:
        no_sum_02 = 0
        to_02_flg = False

# === フラグで、比較文字があった場合は、合計出力
# 比較文字がない場合は、「０」を出力。
if to_02_flg == True:
    print(sum_num_02)
else:
    print(no_sum_02)


# ================================== End

# ================================== Start

"""

入力例1
2
MIDORIKAWA
KIRISHIMA
2
KIRISHIMA 1
KIRISHIMA 2

出力例1
3
0

---

入力例2
3
PAIIZA
PAIZA
PAIIIZA
2
PAIIZA 2
PAIIIZA 3

出力例2
3
2
0

＝＝＝　模範　＝＝＝

n = int(input())
dmg = {}

for i in range(n):
    s = input()
    dmg[s] = 0

m = int(input())

for i in range(m):
    [p, a] = input().split()
    a = int(a)
    dmg[p] += a

names = list(dmg.keys())
names.sort()

for name in names:
    print(dmg[name])

"""

# int 取得
num_03_i = int(input())

# 辞書 初期化
dmg_03 = {}

# {'MIDORIKAWA': 0, 'KIRISHIMA': 0}  という辞書を作成する
for i in range(num_03_i):
    str_03 = input()
    dmg_03[str_03] = 0

# int 取得
num_03_02 = int(input())

for i in range(num_03_02):
    [a, b] = input().split()
    b = int(b)
    dmg_03[a] += b

# key をソートする
# アルファベット順にソート　a b c の昇順
arr_03 = list(dmg_03.keys())
arr_03.sort()


# === 出力 リストを使って、辞書を出力
for val in arr_03:
    print(dmg_03[val])


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


# ================================== Start

# ================================== End
