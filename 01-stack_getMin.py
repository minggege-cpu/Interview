"""
    题目：实现一个特殊的栈 在实现栈的基本功能的同时，在实现返回栈中最小元素的操作
    要求：1：pop、push、getMin操作的时间复杂度都是O(1)
         2:设计的栈类型可以是现成的栈结构

"""


class stack(object):
    def __init__(self):
        self.stack = []         # 实现基本栈结构
        self.minStack = []      # 存储栈最小元素

    def push(self, item):       # 压栈
        if not self.stack:      # 栈为空的情况
            self.stack.append(item)
            self.minStack.append(item)
        else:
            self.stack.append(item)
            if item <= self.minStack[-1]:    # 插入的元素小于或等于最小值栈的元素
                self.minStack.append(item)

    def pop(self):
        if not self.stack:
            print("栈为空")
        else:
            item = self.stack.pop()
            if item == self.minStack[-1]:
                self.minStack.pop()

    def getMin(self):
        if not self.stack:
            print("栈为空")
        else:
            return self.minStack[-1]


if __name__ == "__main__":
    stack = stack()
    stack.push(10)
    stack.push(100)
    stack.push(1)
    stack.push(2)
    print(stack.stack)
    print(stack.getMin())
    stack.pop()
    print(stack.stack)
    print(stack.getMin())
    stack.pop()
    print(stack.stack)
    print(stack.getMin())