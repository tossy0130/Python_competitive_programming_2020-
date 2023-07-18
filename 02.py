############ 文字列 ##############

### ============================ 整数と文字列

####### 文字列の長さを出力
def Integers_And_Strings_01(num):
    
    arr = []
    ### 値取得
    for i in range(num):
        arr.append(input())
    
    ### === 文字列の長さを出力 === 
    for val in arr:
        print(len(val))
        
###========= Integers_And_Strings_01　実行
get_num = int(input())
Integers_And_Strings_01(get_num)
    
### ============================ 整数と文字列 END

### ============================ 部分文字列

### ========= 文字列が含まれているか
def Integers_And_Strings_02(a_str, t_str):
    if a_str in t_str:
        print("YES")
    else:
        print("NO")
        
get_str_02 = input()
get_str_002 = input()

Integers_And_Strings_02(get_str_02, get_str_002)

### ============================ 部分文字列 END

### ============================ 数字の文字列操作

def Integers_And_Strings_03(get_list_03 = []):
    
    a_03 = int(get_list_03[0]) + int(get_list_03[3])
    b_03 = int(get_list_03[1]) + int(get_list_03[2])
    
    print(str(a_03) + str(b_03))
    
### =======　Integers_And_Strings_03　実行

### 1文字ずつ取得
get_list_03 = list(input())

Integers_And_Strings_03(get_list_03)

### ============================ 数字の文字列操作 END

### ============================ 数字の文字列操作（0埋め）

def Integers_And_Strings_04(get_str_04) :
    
    str_num_04 = len(get_str_04)

    if str_num_04 == 1:
        print("00" + str(get_str_04))
    elif str_num_04 == 2:
        print("0" + str(get_str_04))
    else :
        print(str(get_str_04))    
        
### =========== Integers_And_Strings_04 実行

get_str_004 = input()
Integers_And_Strings_04(get_str_004)

### ============================ 数字の文字列操作（0埋め） END

### ============================ 数字の文字列操作（時刻1）

def Integers_And_Strings_05(get_list_05 = []):
    del get_list_05[2]
        
    a_arr = []
    b_arr = []
        
    for i in range(4):
        if i <= 1:
            a_arr.append(get_list_05[i])
        else :
            b_arr.append(get_list_05[i])
    
    if '0' == a_arr[0]:
        print(a_arr[1])
    else:
        print(a_arr[0] + a_arr[1])
        
    if '0' == b_arr[0]:
        print(b_arr[1])
    else:
        print(b_arr[0] + b_arr[1])
        
### ========= Integers_And_Strings_05 

get_list_05 = list(input())
Integers_And_Strings_05(get_list_05)


### ============================  数字の文字列操作（時刻1） END


### ============================ 数字の文字列操作（時刻1）

# 与えられた時刻の 30 分後 を出力

def Integers_And_Strings_06(get_list_06 = []):
    del get_list_06[2]
    
    a_arr = []
    b_arr = []
    
    tmp_s = ''
    
    # === a_arr, get_list_06[0] , [1]    b_arr, get_list_06[2] , [3] 
    for i in range(4):
        if i <= 1:
            a_arr.append(get_list_06[i])
        else :
            b_arr.append(get_list_06[i])
            
    if b_arr[0] == '3':
        a_arr[1] = int(a_arr[1]) + 1
        tmp_s = '0'
    elif b_arr[0] == '4':
        a_arr[1] = int(a_arr[1]) + 1
        tmp_s = '1'
    elif b_arr[0] == '5':
        a_arr[1] = int(a_arr[1]) + 1
        tmp_s = '2'
    else :
        b_arr[0] = int(b_arr[0]) + 3
    
    if not tmp_s:
        print(a_arr[0] + str(a_arr[1]) + ":" + str(b_arr[0]) + b_arr[1])
    else:
        print(a_arr[0] + str(a_arr[1]) + ":" + tmp_s + b_arr[1])
    
        
### ============= 実行
get_list_06 = list(input())

Integers_And_Strings_06(get_list_06)

### ============================ 数字の文字列操作（時刻1） END

### ============================ 文字列 final

def Integers_And_Strings_07(get_num_07):
    for i in range(get_num_07):
        ### 値取得
        [time_str, h_s, m_s] = input().split()
        
        ### 時間を分割
        time_l = int(time_str[:2])
        time_r = int(time_str[3:])
        
        ### int 型へ変換
        h_s = int(h_s)
        m_s = int(m_s)
        
        ### 時間計算
        ans_h = time_l + h_s # 時
        ans_m = time_r + m_s # 分
        
        ### 分が 60 以上だったら
        if ans_m >= 60:
            ans_h += 1
            ans_m -= 60
        
        ### 時間 24 => 0 計算
        if ans_h >= 24:
            ans_h -= 24
            
        ### int => str パース
        ans_h = str(ans_h)
        ans_m = str(ans_m)
        
        ### 0 埋め
        if len(ans_h) == 1:
            ans_h = "0" + ans_h
        if len(ans_m) == 1:
            ans_m = "0" + ans_m
            
        ####### 結果出力
        print(ans_h + ":" + ans_m)
        

### ============ Integers_And_Strings_07 実行  
### ループ回数
get_num_07 = int(input())
Integers_And_Strings_07(get_num_07)

### ============================ 文字列 END