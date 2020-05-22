"""
    输入一个无序的数组  找到其中最长上升序列的长度
    输入 [10, 9, 2, 5, 3, 7, 101, 18]
    输出：4
    解释:最长上升序列  [2, 3, 7, 101]
    说明：可能会有多个上升序列，只需求出最长的那段
    你算法的时间复杂度应该为 O(n^2)
    进阶：将算法的时间复杂度降低到 O(nlogn)
"""


# 时间复杂度为O(n^2)的解法
def getMaxLength(arr):
    n = len(arr)
    dp = [1] * n            # 默认每个元素都为长度为一的上升序列
    for i in range(n):      # 嵌套循环，将待求数组中每个元素与它左边的元素进行比较
        for j in range(i):
            if arr[i] > arr[j]:     # 上升序列   只与左边比它小的元素比较
                dp[i] = max(dp[i], dp[j] + 1)
    return getMax(dp)


# 获取dp列表最大值
def getMax(arr):
    max = 1
    for i in arr:
        if i > max:
            max = i
    return max


if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    print(getMaxLength(arr))



