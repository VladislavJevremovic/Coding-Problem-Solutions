# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
from typing import List

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Codec0:  # slow!
    def serialize(self, root):
        def helper(root, string):
            if not root:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = helper(root.left, string)
                string = helper(root.right, string)

            return string

        return helper(root, '')

    def deserialize(self, data):
        def helper(vals):
            if vals[0] == 'None':
                vals.pop(0)
                return None

            root = TreeNode(vals.pop(0))
            root.left = helper(vals)
            root.right = helper(vals)

            return root

        vals = data.split(',')
        root = helper(vals)

        return root


class Codec1:
    def serialize(self, root: TreeNode) -> str:
        preorder_list = []
        self.preorder(root, preorder_list)

        return " ".join(str(item) for item in preorder_list)

    def deserialize(self, data: str) -> TreeNode:
        data = data.split()
        data.reverse()  # use right pop

        return self.dfs(data)

    def preorder(self, root: TreeNode, preorder_list: List[int]) -> None:
        if not root:
            preorder_list.append(None)
            return

        preorder_list.append(root.val)
        self.preorder(root.left, preorder_list)
        self.preorder(root.right, preorder_list)

    def dfs(self, data: List[str]) -> TreeNode:
        if not data:
            return

        val = data.pop()  # faster to pop off right
        if val == 'None':
            return None
        else:
            root = TreeNode(int(val))

        root.left = self.dfs(data)
        root.right = self.dfs(data)

        return root


class Codec2:
    def serialize(self, root):
        if not root:
            return ''

        q = deque([root])
        vals = []
        while q:
            node = q.popleft()
            if not node:
                vals.append('None')
                continue

            vals.append(str(node.val))
            q.append(node.left)
            q.append(node.right)

        return ",".join(vals)

    def deserialize(self, data):
        if not data:
            return None

        vals = data.split(",")
        nodes = iter((None if v == 'None' else TreeNode(int(v))) for v in vals)
        root = next(nodes)
        q = deque([root])

        while q:
            node = q.popleft()

            left = next(nodes)
            if left:
                node.left = left
                q.append(left)

            right = next(nodes)
            if right:
                node.right = right
                q.append(right)

        return root


def test():
    codec = Codec1()
    codec.deserialize(codec.serialize(TreeNode(0)))

# Input: root = [1,2,3,None,None,4,5]
# Output: [1,2,3,None,None,4,5]
#
# Input: root = []
# Output: []
#
# Input: root = [1]
# Output: [1]
#
# Input: root = [1,2]
# Output: [1,2]
