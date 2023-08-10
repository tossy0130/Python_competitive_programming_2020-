num_01, num_02 = map(int, input().split())

# 配列へ格納する
arr_01 = [int(i) for i in input().split()]
arr_02 = [int(j) for j in input().split()]

ans = 0

# ========= 判定ループ
for i in range(num_01):

    for j in range(num_02):

        tmp = arr_01[i] * arr_02[j]
        print("tmp:::" + str(tmp))

        # 大きい値を入れていく
        if (ans < tmp):
            ans = tmp

print(ans)
