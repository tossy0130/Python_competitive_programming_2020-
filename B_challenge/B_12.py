"""
五目並べ（縦）

入力例1
XXOXO
OXOXX
OOOOO
OXOX.
XOXXO

出力例1
D

入力例2
XXOXO
OXOXX
.OXXO
OXOO.
XXXXX

出力例2
D

"""


ans_str = "D"
### 値取得
for i in range(5):
    get_arr.append(input())
    
### ============ 処理  縦へのループ処理 ============ ###
for i in range(5):
    
    count_num = 0
    target = ''
    
    for j in range(5):
        
        # 比較用に、１列目の文字を取得
        target = get_arr[0][i]
       # print('target ++++++ ' + target)
        
        if target == "":
            target = get_arr[j][i]
        
        if get_arr[j][i] != "." and target == get_arr[j][i]:
            count_num += 1
        #    print("合致::" + get_arr[j][i])
        else:
            break
        
    if count_num == 5:
        ans_str = target
        break
            
print(ans_str)