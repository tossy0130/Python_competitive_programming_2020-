# coding: utf-8
# Your code here!


"""

・sの文字数は5文字
・sに含まれる文字は"O"か"X"か"."のいずれか
・勝者が2人になる盤面が、与えられることはありません。
-------------------

入力例1
OOOOO

出力例1
O

入力例2
OXOOO

出力例2
D

入力例3
...O.

出力例3
D


"""


def Gomoku_09(hantei_num, hantei_str,hantei_str_02, err_str):
    
    hantei_str = 'O'
    hantei_str_02 = 'X'
    err_str = 'D'
    
    get_str_09 = input()
    ans_09 = get_str_09.count(hantei_str)
    ans_09_02 = get_str_09.count(hantei_str_02)
    
    
    if(ans_09 == 5 or ans_09_02 == 5):
        
        if(get_str_09[0] == hantei_str):
            print(hantei_str)
            
        if( get_str_09[0] == hantei_str_02):
            print(hantei_str_02)
        
    else:
        print(err_str)
                

# === 実行
Gomoku_09(5, 'O','X', 'D')

