"""

入力例1
4
1 4
1 5
1 3
2

出力例1
4
4 5
4 5 3
4 5

入力例2
4
1 5
1 3
1 1
2

出力例2
5
5 3
5 3 1
5 3


"""


num = int(input())
# スタック
STA = []

for i in range(num):
    q = input().split()
    if (q[0] == '1'):
        STA.append(q[1])
    
    else:
        STA.pop()
    
    print (" ".join(STA))
    
"""
join 使い方

>>> s = ["A", "B", "C", "D"]
>>> "->".join(s)
'A->B->C->D'

"""

### =====================================

""" 


"""

num_2 = int(input())

S_arr = []

for i in range(num_2):
    t_list = input().split()
    if(t_list[0] == '1'):
        # 1だったら　PUSH 入れる
        S_arr.append(t_list[1])
    else:
        # 1じゃなかったら、POP 出す
        print(S_arr.pop())
    print(" ".join(S_arr)) 

### ===================================== END