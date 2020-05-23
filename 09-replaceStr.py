"""
    给定两个字符串，计算出将s1转化为s2使用的最少操作数
    你可以对一个字符串使用三种操作
    1.插入一个字符
    2.删除一个字符
    3.替换一个字符
    示例：
    输入 s1='horse' s2='ros'
    输出：3
    解释：
    horse➡rorse (h转化为r)
    rorse➡rose(删除r)
    rose➡ros(删除e)
"""


# 添加备忘录消除重叠子问题
def minDistance(s1, s2):
    memo = {}

    def dp(i, j):
        if (i, j) in memo:      # 判断是否为重叠子问题
            return memo[(i, j)]
        if i == -1:             # 有一方到了头 直接将另一个字段的剩余全部按顺序加入
            memo[(i, j)] = j + 1
            return j + 1
        if j == -1:
            memo[(i, j)] = i + 1
            return i + 1
        if s1[i] == s2[j]:      # 当前位置相同 全部往后走一位
            memo[(i, j)] = dp(i-1, j-1)
            return memo[(i, j)]         # 不操作
        else:
            memo[(i, j)] = min(     # 取三个操作中操作步数最少的一步
                dp(i, j-1) + 1,
                dp(i-1, j) + 1,
                dp(i-1, j - 1) + 1
            )
            return memo[(i, j)]

    return dp(len(s1)-1, len(s2)-1)


if __name__ == "__main__":
    s1 = 'rad'
    s2 = 'apple'
    print(minDistance(s1, s2))

