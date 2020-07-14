"""
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1，m<=n），
每段绳子的长度记为k[1],...,k[m]。请问k[1]x...xk[m]可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
"""


# 递归解法
def main(n):
    if n == 2:
        return 1
    elif n == 3:
        return 2

    def dp(n):
        if n in memo:
            return memo[n]
        # 表示此时不分是最大的
        if n <= 4:
            return n
        res = 0
        for i in range(1, n):
            res = max(res, dp(i)*dp(n-i))
        memo[n] = res
        return res
    return dp(n)


# 动态规划
def main2(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    product = [0]*(n+1)
    product[0] = 0
    product[1] = 1
    product[2] = 2
    product[3] = 3
    for i in range(4, n+1):
        res = 0
        for j in range(n//2+1):
            res = max(res, product[j]*product[i-j])
        product[i] = res
    return product[n]


if __name__ == "__main__":
    memo = {}
    n = int(input())
    print(main(n))
    print(main2(n))


