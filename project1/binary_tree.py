"""
1. 实现二叉树，并回答以下问题
二叉树的前、中、后序遍历是什么，仅仅是三个顺序不同的列表吗？
请分析后续遍历有什么特殊之处？
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)
        else:
            pass

    def preorder_traversal(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=" ")


# 示例用法
if __name__ == "__main__":
    tree = BinaryTree()
    elements = [5, 3, 8, 2, 4, 7, 9]
    for element in elements:
        tree.insert(element)

    print("前序遍历：")
    tree.preorder_traversal(tree.root)
    print("\n")

    print("中序遍历：")
    tree.inorder_traversal(tree.root)
    print("\n")

    print("后序遍历：")
    tree.postorder_traversal(tree.root)
    print("\n")

    # 问题一: 二叉树的前、中、后序遍历是什么，仅仅是三个顺序不同的列表吗？
    """
    表现上是三种不同顺序的列表, 在应用场景上有不同
    前序遍历通常用于复制树的结构
    中序遍历在二分搜索树种可以用于对树进行排序
    后序遍历通常用于释放一棵二叉树的内存空间
    """

    # 问题二: 请分析后续(序)遍历有什么特殊之处？
    """
    后续遍历的特点是执行操作时，肯定已经遍历过该节点的左右子节点，
    因此适用于删除等操作
    """

