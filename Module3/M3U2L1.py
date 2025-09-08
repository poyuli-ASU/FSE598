def partition(arr, low, high):
    # 選擇最後一個元素作為 pivot
    pivot = arr[high]
    print(f"選擇的 Pivot: {pivot}")

    i = low - 1  # i 指向小於 pivot 的最後一個元素  => low = 0, i = -1
    for j in range(low, high):  # j > 0 > 1 
        if arr[j] <= pivot:         # 81 <  97
            i += 1                  # i > 0 > 1
            arr[i], arr[j] = arr[j], arr[i] # 69, 81, 30, 38, 9, 2, 47, 61, 32, 79
            print(f"交換: [i], [j] => {i}, {j}")

    # 將 pivot 放到正確位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        # 分割陣列並取得 pivot 位置
        pi = partition(arr, low, high)
        
        # 遞迴排序左半部
        quicksort(arr, low, pi - 1)
        
        # 遞迴排序右半部
        quicksort(arr, pi + 1, high)

# 測試程式
arr = [69, 81, 30, 38, 9, 2, 47, 61, 32, 79]
print("原始陣列:", arr)

quicksort(arr, 0, len(arr) - 1)
print("排序後的陣列:", arr)