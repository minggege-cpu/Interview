"""
    斐波那契数列
    满足f(n)=f(n-1)+f(n-2)的数列
"""


from timeit import Timer


# 实现方法一：暴力递归   缺点：重复计算了很多数据 效率差
def Fibonacci1(N):
    if N == 1 or N == 2:
        return 1
    else:
        return Fibonacci1(N-1) + Fibonacci1(N-2)


# 实现方法二：添加备忘录的递归解法  将已经计算好的记录在备忘录中 如果当前数已经被计算过  直接return 不用再用f(n)=f(n-1)+f(n-2)
def Fibonacci2(N):
    if N == 1 or N == 2:
        return 1
    else:
        if memo[N] != 0:
            return memo[N]
        else:
            memo[N] = Fibonacci2(N-1) + Fibonacci2(N-2)
        return memo[N]


def testFibonacci1():               # 测试函数
    res = []
    for i in range(20):             # 即N
        res.append(Fibonacci1(i + 1))


def testFibonacci2():               # 测试函数
    res = []
    for i in range(20):             # 即N
        res.append(Fibonacci2(i + 1))


if __name__ == "__main__":
    memo = [0] * 21
    time1 = Timer("testFibonacci1()", "from __main__ import testFibonacci1")
    time2 = Timer("testFibonacci2()", "from __main__ import testFibonacci2")
    print("累加所需时间：", time1.timeit(100))  # N=20的斐波那契数列运行100次 0.48560180000000003秒
    print("append所需时间：", time2.timeit(100))  # N=20的斐波那契数列运行100次 0.0005940000000000945秒   由此可见效率相差极大



