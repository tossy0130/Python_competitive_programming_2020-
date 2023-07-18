### ==================== 挿入ソート ====================

### 挿入ソート
def Sentaku_Sort(n, *args):
    
    for i in range(1, n):
        j = i
    ############### 挿入ソート アルゴリズム ###############
        while j >= 1 and arr_l[j - 1] > arr_l[j]:
        
            tmp = arr_l[j - 1]
            arr_l[j - 1] = arr_l[j]
            arr_l[j] = tmp
            j = j - 1
    
        for k in range(n):
            if k == len(arr_l) - 1:
                print(str(arr_l[k]))
            else:
                print(str(arr_l[k]) + ' ', end='')


n = int(input())
### 値取得 4 1 3 5 2
arr_l = list(map(int, input().split()))

########## 挿入ソート　開始
Sentaku_Sort(n, arr_l)

############################　挿入ソート END ===========================
        
        




