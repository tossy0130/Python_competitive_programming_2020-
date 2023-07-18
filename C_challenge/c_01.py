# ================================== Start
"""

N M K
a_{1,1} ... a_{1,M}
...
a_{N,1} ... a_{N,M}

-------------

入力例1
3 2 1
2 2
1 2
1 1

出力例1
0
1
2

入力例2
4 5 2
1 3 4 4 5
2 2 2 2 2
1 2 3 4 5
1 1 1 1 1

出力例2
0
5
1
0

"""

N, M, K = map(int, input().split())

for i in range(N):
    a = [int(j) for j in input().split()]
    ans = 0
    for j in range(M):
        if a[j] == K:
            ans += 1
    print(ans)

# ================================== End

# ================================== Start

"""

入力例1
2
4
3

出力例1
4
3


"""

n = int(input())
a = [0] * n

for i in range(n):
    a[i] = int(input())

a.sort(reverse=True)

for i in range(n):
    print(a[i])


# ================================== End

# ================================== Start

"""

入力例1
2
1 3
2 2

出力例1
2 2
1 3

"""

n_02 = int(input())

arr_02 = []
for i in range(n_02):
    a, b = input().split()
    # === ２次元配列　で 取得
    arr_02.append([int(a), int(b)])

# === ２次元配列でソートする　
arr_02.sort(reverse=True)

# === ２次元配列 => リストへ戻して　出力
for i in range(n_02):
    [a, b] = arr_02[i]
    print(a, b)


# ================================== End

# ================================== Start

"""

入力例1
2
2 1
1 2

出力例1
1 2
2 1

入力例2
4
2 3
0 4
5 0
3 3

出力例2
0 4
3 3
2 3
5 0

"""

# ============== 入れ替えてソートする
n_03 = int(input())

arr_03 = []
for i in range(n_03):
    a, b = input().split()
    # === ２次元配列　で 取得
    arr_03.append([int(b), int(a)])

# 昇順
arr_03.sort(reverse=True)

for i in range(n_03):
    [a, b] = arr_03[i]
    print(b, a)


# ================================== End

# ================================== Start

# ================================== End

# ================================== Start

# ================================== End

# ================================== Start

# ================================== End
