class Node:
    """定義二叉樹的節點"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    """定義二叉樹的操作"""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """插入新節點"""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        else:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)

    def inorder_traversal(self):
        """中序遍歷"""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)
# 建立並操作二叉樹
tree = BinaryTree()
for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    tree.insert(value)

# 顯示中序遍歷結果
print("中序遍歷結果:", tree.inorder_traversal())
