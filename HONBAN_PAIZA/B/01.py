"""

入力例1
4
y n
n y
n n
y y

出力例1
3
1
2
3

入力例2
1
y y

出力例2
0

"""

num = int(input())

ans_arr = []

# 全体のループの回数を設定する。
for i in range(num):
    
    tmp = input()
    tt = tmp.replace(' ', '') # 文字列の空白を除去する
    
    count = 0
    idx_num = 0
    
    # １行ずつ回す
    for j in tt:
        # 文字列 n があったらカウントアップ
        if j == 'n':
            count += 1
            idx_num = i + 1 # 取得した index にプラス 1をする。
        
        # カウントが 0じゃなかったら、index + 1を入れて、breakする。
        if count != 0:
            ans_arr.append(idx_num)
            break

arr_len = len(ans_arr) # 配列の長さを取得させる
ans_arr.insert(0, arr_len) # 配列の頭に、配列の長さを挿入

for ans in ans_arr:
    print(ans)