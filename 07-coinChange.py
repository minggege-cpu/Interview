"""
    凑零钱问题
    给你 k 种⾯值的硬币，⾯值分别为 c1, c2 ... ck ，每种硬币的数量⽆限
    再给⼀个总⾦额 amount ，问你最少需要⼏枚硬币凑出这个⾦额
    如果不可能凑出，算法返回 -1
    思路：
    这是个动态规划问题 因为它具有最优子结构
    先确定「状态」
    然后确定 dp 函数的定义
    然后确定「选择」并择优
    例如：硬币的金额有三种 面额为 1 2 5 总金额amount=11
    那么最少需要三枚硬币才能凑出  即 5 5 1
"""


# 暴力递归
def coinChange1(coins, amount):
    def dp(amount):
        if amount == 0:         # 完成凑钱
            return 0            # 不能凑出
        elif amount < 0:
            return -1
        else:
            res = float('INF')      # 设需要无穷大次数凑出
            for coin in coins:
                sub = dp(amount - coin)     # 递归求最小次数
                if sub == -1:
                    continue
                else:
                    res = min(res, 1 + sub)     # 等于上一次再加上一次
            return res if res != float("INF") else -1
    return dp(amount)


# 添加备忘录 减少了递归执行次数
def coinChange2(coins, amount):
    def dp(amount):
        if amount in memo:
            return memo[amount]
        if amount == 0:         # 完成凑钱
            return 0            # 不能凑出
        elif amount < 0:
            return -1
        else:
            res = float('INF')      # 设需要无穷大次数凑出
            for coin in coins:
                sub = dp(amount - coin)     # 递归求最小次数
                if sub == -1:
                    continue
                else:
                    res = min(res, 1 + sub)     # 等于上一次再加上一次
            memo[amount] = res if res != float("INF") else -1
            return memo[amount]
    return dp(amount)


if __name__ == "__main__":
    memo = dict()
    coins = [1, 2, 5]
    print(coinChange2(coins, 18))



