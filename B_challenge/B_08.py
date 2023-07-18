"""

入力例1
XXOXO
OXOXX
OOOOO
OXOX.
XOXXO

出力例1
XXOXO
OXOXX
OOOOO
OXOX.
XOXXO

入力例2
XXOXO
OXOXX
.OXXO
OXOO.
XXXXX

出力例2
XXOXO
OXOXX
.OXXO
OXOO.
XXXXX
    
"""
    
# === 5 × 5　のマスを出力
def Loop_08(num):
     for i in range(num):
         str_08 = input() # １行 取得
         print(str_08) # １行 出力
         
# === 実行     
Loop_08(5)