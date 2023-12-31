"""

10000 以上かつ 13 で割り切れるような最小の自然数

"""

num_01 = input()

for i in range(10000, 20000):
    if i % 13 == 0 :
        print(i)
        break
    
### 出力 10010

# =============================================

"""

パイザ君と霧島京子は最初どちらも数 1 をもっています。
パイザ君は自分の番が来ると、自分のもっている数の a 倍を霧島京子の
数に足してあげます。霧島京子は自分の番が来ると、自分のもっている数
を b で割った余りをパイザ君の数に足してあげます。
この手続きをパイザ君の番から始めて、
霧島京子の数がnより大きくなるまで繰り返します。

手続きが終わったときのパイザ君の操作回数を求めてください。

入力例1
6
3 2

出力例1
2

"""

n = int(input())
a, b = map(int, input().split())

pai = 1
kyou = 1

idx = 0
while (kyou <= n):
    
    idx += 1
    
    kyou += pai * a  # 自分のもっている数の a 倍を霧島京子の数に足す
    
    if kyou > n :
        break
  
    pai += kyou % b # 自分のもっている数を b で割った余りをパイザ君の数に足す
    
print(idx)




