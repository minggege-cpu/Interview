"""
    题目：如何仅用递归函数的栈逆序一个栈
    要求：必须使用递归
"""


class stack(object):

    def __init__(self):
        self.stack = []         # 实现基本栈结构
        self.reserveStack = []  # 存储逆序栈

    def push(self, item):       # 压栈
        self.stack.append(item)

    def pop(self):              # 出栈
        if not self.stack:
            print("栈为空")
        else:
            self.stack.pop()

    def reverse(self):          # 逆序栈
        while self.stack:       # 原栈为空时跳出循环
            item = self.stack.pop()
            self.reserveStack.append(item)
            return self.reverse()   # 递归执行


if __name__ == "__main__":
    stack = stack()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.reverse()
    print(stack.reserveStack)



