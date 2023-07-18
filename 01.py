
### ============================ 単純な入出力
def Print_Line_01(str): {
    print(str)
}

#=== Print_Line_01 実行
input = input()
Print_Line_01(input)
#=== Print_Line_01 実行　END

### ============================ 単純な入出力 END

### ============================ 複数行にわたる出力
def Print_Line_02(p, num):
    i = 0
    while (i < num):
        print(p)
        i = i + 1
        
input_02 = int(input())

Print_Line_02("paiza", input_02)
### ============================ 複数行にわたる出力 END

### ============================ 複数行にわたる入力
def Print_Line_03(num):
    
    arr = []
    for i in range(num):
        arr.append(int(input()))
    
    ### 出力
    for item in arr:
        print(item)
    
### Print_Line_03実行
num = int(input())
Print_Line_03(num)
### ============================ 複数行にわたる入力 END 

### ============================ 入力の配列による保持

def Print_Line_MAX_04(num):
    arr = []
    ######### ========== 複数行挿入
    for i in range(num):
        arr.append(int(input()))
    
    ######### ==========
    ans_max = max(arr)
    print(ans_max)
     
### Print_Line_MAX_04 実行
get_num_01 = int(input())
Print_Line_MAX_04(get_num_01)


### ============================ 入力の配列による保持 END

### ============================ 半角スペース区切りでの出力
def Print_Line_05(num):
    for i in range(num):
        if i == num - 1:
            print("paiza", end="")
        else:
            print("paiza" + " " , end="")
            

######### Print_Line_05 実行
get_num_02 = int(input())

Print_Line_05(get_num_02)

### ============================ 半角スペース区切りでの出力 END

### ============================ 改行区切りでの出力

def Print_Line_06():
    
   ### 2行目取得 
   """
   4 30 12
   """
   arr_a = list(map(int, input().split()))
   for val in arr_a :
       print(val)
        
get_num_03 = int(input())

Print_Line_06()

### ============================ 改行区切りでの出力 END

### ============================ 標準入出力

''' 
    入力例2
    3
    Tanaka 18
    Sato 50
    Suzuki 120

    list_01[0][0] = Tanaka , list_01[0][1] = 18
    list_01[1][0] = Sato , list_01[1][1] = 50
    list_01[2][0] = Suzuki , list_01[2][1] = 120

'''

def Print_list_01(num):
    
    ### 2次元配列で取得  
    list_01 = []
    for i in range(num):
        a,b = input().split()
        list_01.append([a, int(b)])
        
        ### プラス 1 処理
        for idx in range(num):
            list_01[idx][1] = list_01[idx][1] + 1
        
        ### 出力
        for j in range(num):
            print(list_01[j][0] + " " + str(list_01[j][1]))

######### Print_list_01 実行 
get_num_04 = int(input())
Print_list_01(get_num_04)

### ============================ 標準入出力 END

### ============================ 文字列 last


### ============================ 文字列 last END
