#=========================== Start
""" 

入力例1
5-5 11 3 -9 0-4

出力例1
-5

"""
n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

answer = -101
for val in a:
    if val <= k:
        answer = max(answer, val)

print(answer)

#=========================== END

#=========================== Start
"""
入力例1
5-5 11 3 -9 0-4

出力例1
0
    
"""
a_num = int(input())
a_list = [int(x) for x in input().split()]
b_num = int(input())

ans_list = []
for i in range(a_num):
    if a_list[i] > b_num :
        tmp = a_list[i]
        ans_list.append(tmp)
        
print(min(ans_list))

#=========================== END

#=========================== Start
"""
入力例1
5
-3  2  0  -1  2
2
"""
n = int(input()) # １行目取得
arr_a = list(map(int, input().split())) # ２行目取得
c = int(input()) # ３行目

a_sum = 0 # 合計格納

for i in range(n):
    if c == arr_a[i]:
        a_sum += 1
    else:
        pass
    
print(a_sum)

#=========================== END

#=========================== Start
"""
入力例1
5-3 2 0 -1 22

出力例1
2
"""

a = int(input())
arr_list = list(map(int, input().split()))
b = int(input())

s = 0
for i in range(a):
    if arr_list[i] == b:
        s = i + 1
        break

print(s)

#=========================== END

#=========================== Start
"""
入力例1

5-3 2 0 -1 22

出力例1

5
"""
a = int(input())
a_arr = [int(x) for x in input().split()]
target = int(input())

sum_a = 0
for i in range(a -1, -1, -1):
    if a_arr[i] == target:
       sum_a = i + 1
       break
        
print(sum_a)
#=========================== END

#=========================== Start

"""
入力例1
5 -3 2 0 -1 22

出力例1
25

"""
a = int(input())
b_arr = [int(x) for x in input().split()]
c_target = int(input())

sum_arr = []
for i in range(a):
    if b_arr[i] == c_target:
        tmp = i + 1
        sum_arr.append(tmp)
        
for t in sum_arr:
    print(t)

#=========================== END

#=========================== Start

"""

入力例1
-11 10

出力例1
10 -11

"""

### 値取得　-11 10
a_list = [int(x) for x in input().split()]

a_max = max(a_list)
a_min = min(a_list)

### f string で出力
print(f'{a_max} {a_min}')

#=========================== END

#=========================== Start

"""
入力例1
51 3 5 6 8

出力例1
4
"""

a = int(input())
a_list = [int(x) for x in input().split()]

b = 0
######## 最初の偶数でループを止める
for i in range(a):
    if a_list[i] % 2 == 0:
        b = i + 1
        break
        
print(b)

#=========================== END


#=========================== Start

"""
入力例1
51 3 5 6 8

出力例1
3
"""
a = int(input())
a_list = [int(x) for x in input().split()]

a_int = 0
############## 配列の末尾から、奇数のindex でbreak
for i in range(a - 1, -1, -1):
    if a_list[i] % 3 == 0:
        a_int = i
        break
    
print(a_int)
#=========================== END


#=========================== Start

"""

oxo
oox
oxo
xxx 

"""

H, W = map(int, input().split())

####### ２次元配列で取得
arr_h = []

for h in range(H):
    array = list(map(str, input()))
    arr_h.append(array)
    
####### ２次元配列で取得
arr_ww = []

for w in range(H):
    array_tmp = list(map(int, input().split()))
    arr_ww.append(array_tmp)


arr_ans = []

for i in range(H):
    for j in range(W):
        if arr_h[i][j] == 'o':
           arr_ans.append(arr_ww[i][j])

print(sum(arr_ans))

#=========================== END

#=========================== Start

"""


"""

N, D = map(int, input().split())

t_arr = []
t_arr.append(D)

for i in range(N - 1):
    tmp = int(input())
    t_arr.append(tmp)

ans = []
for j in range(len(t_arr)):
    if j == 0:
        ans.append(t_arr[0])
    
    else:
        tmp = D - t_arr[j]
        ans.append(tmp)
        
go = sum(ans)
print(D * go)

#=========================== END

#=========================== Start

"""


"""

s = input().strip()

### + で 分割した　配列取得
l_list = s.split('+')

l_num = 0
ll_num = 0

list_len = len(l_list)

t_list = [0] * list_len
tt_list = [0] * list_len

### 文字列　カウント
for i in range(len(l_list)):
   t_list[i] = l_list[i].count('/')
   tt_list[i] = l_list[i].count('<')

### １の桁
ans_l = 0   
for j in t_list:
    ans_l += j
    
### 10 の桁
ans_ll = 0
for jj in tt_list:
    ans_ll += jj * 10
    
print(ans_ll + ans_l)

#=========================== END

#=========================== Start

"""

"""

l_num = int(input())

get_list = [input() for x in range(l_num)]

### 重複削除
s_list = list(set(get_list))

### あいこ判定
if len(s_list) > 2 :
    print('draw')

### じゃんけん判定
else:
    if 'paper' in s_list and 'rock' in s_list:
        print('paper')
    elif 'rock' in s_list and 'scissors' in s_list:
        print('rock')
    elif  'paper' in s_list and 'scissors' in s_list :
        print('scissors')
    else:
        print('draw')

#=========================== END

#=========================== Start

"""


"""

num, num_1, num_2 = map(int, input().split())

### 対象リスト
list_item = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

#######  *list_item, sep='' で　出力すると [A,B]  の []　を外して　出力する
print(*list_item[:num], sep='')

#######  
print(*list_item[num:num + num_1], sep='')

print(*list_item[num + num_1:num + num_1 + num_2], sep='')

#=========================== END

#=========================== Start

"""
N
s1 t1 u1
s2 t2 u2
s3 t3 u3
...
sn tn un

"""

# 行数
N = int(input().strip())


# 2次元配列
grid = []
for i in range(N):
    array = list(map(int, input().strip().split()))
    grid.append(array)

#=========================== END

#=========================== Start

"""

"""

m,n = map(int, input().split()) # 値取得    

##################### def 開始
def func(m, n):
    arr_item = []
    
    ###### 値を 1 4 7 10 13 16 19 22 25 28 を list に格納
    if m == n :
        for i in range(m, n * 11, n):
            tmp = str(i)
            arr_item.append(tmp)
    else:
         for i in range(m, n * 10, n):
            tmp = str(i)
            arr_item.append(tmp)
    
    ############### 最後の要素だけ　空白行を取る
    for i,e in enumerate(arr_item):
        if i == len(arr_item) -1:
            print(e)
        else:
            print(e, end=' ')
            
func(m,n)

#=========================== END

#=========================== Start

"""


"""

def func(num):
       
    # ループで取得
    arr_item = [input() for i in range(num)]
    # 判定
    # i = 0,1,2  indexが入る e = 値 Paiza , Gino
    for i,e in enumerate(arr_item):
           if i != len(arr_item) -1: # エミュレーターでリストの最後の要素を取得
               print(e, ',' , sep='', end='') # sep='' => スペースなし, 
           else:
               print(e, '.', sep='')
               
###### 出力用 #########
loop_num = int(input())
print('Hello' + ' ' , end='')
func(loop_num)

#=========================== END

#=========================== Start

"""

"""

def func(n):
    for i in range(1,10):
      if i == 9 :
        print(n * i, end = '') # 9 の時は改行をつける
      else:
        print(n * i, end=' ') # 9 以外は　改行をつけない
        
ans = int(input())

###　関数 実行
func(ans)

#=========================== END


#=========================== Start

"""

"""

def func(num_1, num_2):
    if num_1 > num_2:
       print(num_1)
    elif num_2 > num_1:
       print(num_2)
    else :
       print('eq')
        
a, b = map(int, input().split())

func(a, b)

#=========================== END

#=========================== Start

"""

入力例1
3
1 1024
11 2048
21 4196

出力例1
71

"""

loop = int(input())

a = []
b = []

########## 1行ずつ　list で　取得する   tmp,tmp_02 = map(int, input().split())
for i in range(loop):
        tmp,tmp_02 = map(int, input().split())
        a.append(tmp) # 1行目取得
        b.append(tmp_02) # 2行目取得
# print(a)
# print(b)
n = 0

ans = 0
ans_02 = 0
ans_03 = 0

######## int で切り捨て
for nn in range(len(a)):
    
    if '5' in str(a[nn]):
        ans += (b[nn] / 100 * 5)  # 5% の計算
    elif '3' in str(a[nn]):
        ans_02 += (b[nn] / 100 * 3) # 3% の計算
    else:
        ans_03 += int(b[nn] / 100 * 1) #　1% の計算
        
print(int(ans) + int(ans_02) + int(ans_03))

#=========================== END

#=========================== Start

"""

入力例1

1
paiza
paizaonlinehackathon

出力例1

paizaonlinehackathon


"""

num = int(input())
trget = str(input())

t = []

"""
ai
pizza
paiza
aizu
ai
sai
"""
# 値をリストへ格納
t = [input() for i in range(num)]

ans = []
for g in t :
    if trget in g:
        ans.append(g)
        
# リストが　空か判定 not

if not ans:
    print('None')

else:
    for a in ans :
        print(a)

#=========================== END

#=========================== Start

"""
入力例

12
january januarry
february febrary
march march
april aplil
may may
june june
july jury
august ougust
september septenber
october october
november novembar
december dicembar

出力例
13

"""

N = int(input())

str_list = []
for i in range(N):
    array = list(map(str, input().split()))
    str_list.append(array)

### 多重ループにすると、１文字ずつの出力になる
for nn in str_list:
    # 値が同じだった場合
   if nn[0] == nn[1]:  
       print('2')
   # 文字の長さが違った場合
   elif len(nn[0]) != len(nn[1]):
       print('0')
   # 文字の長さが同じで、値が違った場合
   elif len(nn[0]) == len(nn[1]) and nn[0] != nn[1] :
       for ii in nn :
         print(ii[2])

#=========================== END


#=========================== Start

"""

"""

a, b = map(int, input().split())

arr_1 = []
arr_2 = []

arr_3 = []

if a == 1:
    print('0')
else:
    for i in range(a):
        array = list(map(int, input().split()))
        arr_1.append(array)
    
for n in arr_1:
    if n[0] <= 127:
        arr_2.append('0')
    elif n[0] >= 128:
        arr_2.append('1')
        

for nn in arr_1:
    if nn[1] <= 127:
        arr_3.append('0')
    elif nn[1] >= 128:
        arr_3.append('1')
        
for i in range(len(arr_2)):
    print(arr_2[i] + ' ' + arr_3[i])

#=========================== END


#=========================== Start

"""
入力例
4
5
101
204
301
401
501

出力例
101
301
501

"""

n = int(input())
m = int(input())

arr_i = []
for i in range(m):
    tmp = int(input())
    arr_i.append(tmp)

ans = [] 

for nn in arr_i:
    # not in で、n が　nn に含まれていないか判定
    if str(n) not in str(nn):
        ans.append(str(nn))
        
# 配列が空か調べる
if not ans :
    print('none')
else :
    for a in ans :
        print(a)

#=========================== END

#=========================== Start

"""

"""

N,R = map(int, input().split())

# int 型で　リストで１行　値取得
arr_i = []
for i in range(N):
    # 5, 15, 10 
        tmp = int(input())
        arr_i.append(tmp)

#　最大値取得
max_num = max(arr_i)

print(max_num)

#=========================== END

#=========================== Start

"""

"""

N = int(input())

l_list = []
for i in range(N + 1):
   array = list(map(str, input().strip().split()))
   l_list.append(array)
   
"""
num_list に格納

tokyo 9
beijing 8
singapore 7
london 0
newyork -5
osaka 9
singapore 19:38
"""
num_list = []
for n in l_list:
         # 数字だけ取得 
         num_list.append(n[1])

"""        
for nn in num_list:
    print("nn" + nn)
"""

# num_list へ　格納   
"""
9
8
7
0
-5
9
19:38
"""
# 最後の要素取得
get_list = num_list.pop(-1)
# :00 を取得
get_str = get_list[2:5]

#### 比較判定用　
ans_list = []
for j in num_list:
    if int(j) < 0 :
        ans_list.append(12 + int(j)) 
    elif int(j) == 24:
        ans_list.append(int(0))
    elif int(j) > 12 :
        ans_list.append(int(j) - 12)
    else:
        ans_list.append(12 + int(j))
        
#### 出力
for jj in ans_list:
    if jj < 10:
        print(str(0) + str(jj) + get_str)
    elif jj == 24:
        print(str(0) + str(0) + get_str)
    else :
        print(str(jj) + get_str)

#=========================== END

#=========================== Start

"""

"""

N,Y = map(int, input().split())

# print(N, Y)

a = 0

for i in range(N + 1) :
    # print(i)
     for j in range(N - i + 1):
            a = N - i - j
        #	print('a' + str(a))
        #	print('j' + str(j))
            if i * 10000 + j * 5000 + a * 1000 == Y:
                print(i,j,a)
                exit()
print(-1, -1, -1)

#=========================== END

#=========================== Start

"""
入力例
5
ai
pizza
paiza
aizu
ai
sai

出力例
paiza
aizu
ai
sai

"""

N = int(input())
G = input().strip()

l_list = [input() for i in range(N)]

# print(N, G)

ans = []
sum_i = 0
for i in l_list: 
    if G in i: # リストに G が含まれていたら
        ans.append(i) #リストへ要素を追加する

if not ans : # リストが空なら
    print('None')

else:
    for n in ans :
        print(n)

#=========================== END