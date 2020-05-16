
"""
    用一个栈辅助实现另一个栈的排序
"""


class sortStackByStack(object):

    def __init__(self, stack):
        self.stack = stack      # 要排序的栈
        self.help_stack = []    # 辅助排序的栈

    def sort(self):
        while self.stack:
            if not self.help_stack:         # 辅助栈为空
                self.help_stack.append(self.stack.pop())    # 将stack栈底元素压入辅助栈
            else:
                cur = self.stack.pop()                      # 弹出stack栈底元素
                if cur <= self.help_stack[-1]:              # stack栈底元素小于辅助栈栈底元素
                    self.help_stack.append(cur)             # 将stack栈底元素加入辅助栈
                else:                                       # stack栈底元素大于辅助栈栈底元素时 将cur依次与辅助栈的元素比较
                    while self.help_stack:                  # 直至出现比cur大的元素或者辅助栈为空时 再将cur插入栈
                        help_cur = self.help_stack[-1]
                        if help_cur < cur:
                            self.stack.append(self.help_stack.pop())
                        else:
                            self.help_stack.append(cur)
                            break
        return self.help_stack


if __name__ == "__main__":
    stack = [3, 1, 4, 8, 5, 13,  2, 100]
    s = sortStackByStack(stack)
    print(s.sort())


