"""
    题目：
    你面前有一栋从 1 到 N 共 N 层的楼，然后给你 K 个鸡蛋（K 至少为 1）。
    现在确定这栋楼存在楼层 0 <= F <= N，在这层楼将鸡蛋扔下去，鸡蛋恰好没摔碎（高于 F 的楼层都会碎，低于 F 的楼层都不会碎）。
    现在问你，最坏情况下，你至少要扔几次鸡蛋，才能确定这个楼层 F 呢？
"""


def eggDrop(k, n):
    # 添加备忘录
    memo = {}

    def dp(k, n):
        if k == 1:      # 如果鸡蛋个数为一  只能全部扫描
            return n
        if n == 0:      # 楼层为0返回0
            return 0
        if (k, n) in memo:      # 避免重复计算
            return memo[(k, n)]
        res = float('INF')      # 默认无穷大
        for i in range(1, n+1):     # 循环每个楼层
            res = min(          # 最坏情况下的最少次数
                res, max(
                    dp(k-1, i-1), dp(k, n - i)
                ) + 1
            )
        memo[(k, n)] = res
        return res

    return dp(k, n)


if __name__ == "__main__":
    print(eggDrop(2, 100))


