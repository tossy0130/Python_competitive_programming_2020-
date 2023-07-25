""" 

入力例1
XXOXO
OXOXX
OOOOO
OXOX.
XOXXO

出力例1
O

入力例2
XXOXO
OXOXX
.OXXO
OXOO.
XXXXX

出力例2
X

"""

ans_str = 'D'

for i in range(5):
    arr_08 = input()
    tmp_08 = arr_08[0]
    
    ans_count = 0
    
    for j in arr_08:
        
        if j != '.' and j == tmp_08 :
            ans_count += 1
        else :
            break
    
    # === ５つ並んだ場合は、○ か × を入れる
    if ans_count == 5:
        ans_str = tmp_08

# === 5つ並ばなかったら、デフォルトの D を出力 
print(ans_str)
        
