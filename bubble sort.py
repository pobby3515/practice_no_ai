"""從第一個元素開始，比較第 i 個和第 i+1 個。

如果前者比後者大，就交換它們。

一輪走訪結束後，最大的元素會被放到最後面。

接著只處理前面還沒排序好的部分，重複以上步驟，直到完成排序"""
import random
list_num = set()
while len(list_num) < 10:
    a = random.randint(1,100)
    list_num.add(a)
list_num = list(list_num)
print("原始資料:",list_num)


for a in range(len(list_num)):
    i=0
    while i+1 < len(list_num):
        if list_num[i] < list_num[i+1]:
            i += 1
        else:
            list_num[i], list_num[i+1] = list_num[i+1], list_num[i]
            i += 1
    print(f"過程{a+1}:",list_num)

print("結果:",list_num)