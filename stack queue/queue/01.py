""" 

入力例1
4
1 1
1 4
1 2
2

出力例1
1
1 4
1 4 2
4 2

入力例2
4
1 5
2
1 4
2

出力例2
5

4


"""

import queue

Q = int(input())

q = queue.Queue()  # キュー本体
for i in range(Q):
    query = input().split()
    if query[0] == "1":
        # PUSH
        q.put(query[1])
    elif query[0] == "2":
        # POP
        q.get()
    for j in range(q.qsize()):  # キューの要素分だけループを回す
        tmp = q.get()
        if j < q.qsize():
            print(tmp, end=" ")
        else:
            print(tmp, end="")
        q.put(tmp)
    print()