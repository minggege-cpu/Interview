"""
    通过前序遍历和中序遍历的顺序得到该二叉树
    测试数据
    二叉树
                    13
                15      18
             7        17  20
              9             21

    前序遍历：13 15 7 9 18 17 20 21          根  左  右
    中序遍历：7 9 15 13 17 18 20 21          左  根  右
    后序遍历应当为：9 7 15 17 21 20 18 13     左  右  根
"""


# 存储节点
class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self, preorder, inorder):
        self.preorder = preorder        # 先序遍历
        self.inorder = inorder          # 中序遍历
        self.root = Node(preorder[0])   # 根节点为先序遍历第一个元素
        self.generateTree(self.root, self.preorder, self.inorder)

    # 获取节点在中序遍历中的下标
    def getInorderIndex(self, node, inorder):
        return inorder.index(node.data)

    # 获取节点在先序遍历中的下标
    def getPreorderIndex(self, node, preorder):
        return preorder.index(node.data)

    # 核心算法
    def generateTree(self, node, preorder, inorder):
        if not node:
            return
        index1 = self.getInorderIndex(node, inorder)        # 获取节点中序下标
        index2 = self.getPreorderIndex(node, preorder)      # 获取节点先序下标
        node_lchild = inorder[:index1]                      # 中序遍历列表节点左部均为左子树
        node_rchild = inorder[index1+1:]                    # 中序遍历列表节点右部均为右子树
        if len(node_lchild):                                # 左子树不为空
            node.lchild = Node(preorder[index2+1])          # 先序遍历节点左边一位即为左子树
        if len(node_rchild):                                # 右子树不为空
            node.rchild = Node(preorder[len(node_lchild)+1])    # 先序遍历除去左子树后第一个即为右子树
        # 递归求该节点的左孩子和右孩子的子树，并且调整先序遍历和中序遍历列表
        self.generateTree(node.lchild, preorder[index2+1:index2+len(node_lchild)+1], inorder[:index1])
        self.generateTree(node.rchild, preorder[index2+len(node_lchild)+1:], inorder[index1+1:])

    # 递归输出后序遍历
    def postInorder(self, node):
        if node is None:
            return
        self.postInorder(node.lchild)
        self.postInorder(node.rchild)
        print(node.data, end=" ")


if __name__ == '__main__':
    preorder = [13, 15, 7, 9, 18, 17, 20, 21]        # 前序遍历
    inorder = [7, 9, 15, 13, 17, 18, 20, 21]         # 中序遍历
    tree = Tree(preorder, inorder)
    tree.postInorder(tree.root)



