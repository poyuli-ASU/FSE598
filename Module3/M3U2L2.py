def heapify(arr, n, i):
    """
    將以索引 i 為根的子樹轉換成最大堆。
    arr: 陣列
    n: 堆的大小
    i: 根節點的索引
    """
    largest = i          # 初始化最大值為根節點
    left = 2 * i + 1     # 左子節點索引
    right = 2 * i + 2    # 右子節點索引

    # 如果左子節點存在且大於根節點
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 如果右子節點存在且大於目前最大值
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大值不是根節點，交換並遞迴堆化
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交換
        heapify(arr, n, largest)                     # 遞迴堆化

def heap_sort(arr):
    """
    執行堆排序。
    arr: 要排序的陣列
    """
    n = len(arr)

    # 建立最大堆（從最後一個非葉節點開始）
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 一個個將最大值移到陣列尾端，並重新堆化
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 將最大值移到尾端
        heapify(arr, i, 0)               # 對剩下的堆進行堆化

# 範例陣列
data = [12, 11, 13, 5, 6, 7]

# 執行堆排序
heap_sort(data)

# 顯示排序結果
print("排序後的陣列:", data)
