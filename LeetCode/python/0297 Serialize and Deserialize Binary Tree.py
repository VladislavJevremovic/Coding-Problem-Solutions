# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
from collections import deque
from typing import List

from python.Helpers.BinarySearchTree import BinarySearchNode

TreeNode = BinarySearchNode


class Codec0:  # slow!
    """Recursive preorder string codec: emit values with 'None' placeholders,
    then rebuild by consuming that preorder stream. n = number of nodes."""

    def serialize(self, root):
        # Time: O(n^2) due to repeated string concatenation   Space: O(n)
        def helper(root, string):
            if not root:
                string += "None,"
            else:
                string += str(root.val) + ","
                string = helper(root.left, string)
                string = helper(root.right, string)

            return string

        return helper(root, "")

    def deserialize(self, data):
        # Time: O(n^2) due to repeated list pop(0)   Space: O(n)
        def helper(vals):
            if vals[0] == "None":
                vals.pop(0)
                return None

            root = TreeNode(vals.pop(0))
            root.left = helper(vals)
            root.right = helper(vals)

            return root

        vals = data.split(",")
        root = helper(vals)

        return root


class Codec1:
    """Preorder codec collecting values into a list (None for empty children),
    joined by spaces; deserialize pops from the reversed list. n = nodes."""

    def serialize(self, root: TreeNode) -> str:
        # Time: O(n)   Space: O(n)
        preorder_list = []
        self.preorder(root, preorder_list)

        return " ".join(str(item) for item in preorder_list)

    def deserialize(self, data: str) -> TreeNode:
        # Time: O(n)   Space: O(n)
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
        if val == "None":
            return None
        else:
            root = TreeNode(int(val))

        root.left = self.dfs(data)
        root.right = self.dfs(data)

        return root


class Codec2:
    """Level-order (BFS) codec using a queue with 'None' markers; deserialize
    rebuilds level by level by attaching the next two nodes. n = nodes."""

    def serialize(self, root):
        # Time: O(n)   Space: O(n)
        if not root:
            return ""

        q = deque([root])
        vals = []
        while q:
            node = q.popleft()
            if not node:
                vals.append("None")
                continue

            vals.append(str(node.val))
            q.append(node.left)
            q.append(node.right)

        return ",".join(vals)

    def deserialize(self, data):
        # Time: O(n)   Space: O(n)
        if not data:
            return None

        vals = data.split(",")
        nodes = iter((None if v == "None" else TreeNode(int(v))) for v in vals)
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
