"""
    请实现一个函数
    输入：整型数组arr 窗口大小为w
    输出：一个长度为n-w+1的数组res res[i]表示每一个窗口状态下的最大值
"""


def getMaxWindow(arr, w):
    if (not arr) or (w < 1) or (len(arr) < w):  # 数组为空或者窗口大小违规
        return None
    max_index = []          # 用于存储下标
    res = []                # 存储结果
    for i in range(len(arr)):
        while max_index and (arr[max_index[-1]] <= arr[i]):     # 属于同一个窗口的元素之间比较
            max_index.pop()                                     # 之前入队的找到了更大的  出队
        max_index.append(i)                                     # 下标入队
        if max_index[0] == i-w:                                 # 窗口过期的情况
            max_index.pop(0)                                    # 弹出过期窗口的元素下标即新的窗口下标集合不在包含这个元素的下标
        if i >= w - 1:                                          # 过了一个窗口就可以加入了
            res.append(arr[max_index[0]])                       # 加入结果集
    return res


if __name__ == "__main__":
    arr = [4, 3, 5, 4, 3, 3, 6, 7]
    print(getMaxWindow(arr, 3))


