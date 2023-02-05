# https://leetcode.com/problems/delete-node-in-a-bst/

from python.Helpers.BinarySearchTree import *

TreeNode = BinarySearchNode


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            # find successor in right subtree
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val  # replace with successor value
            root.right = self.deleteNode(root.right, root.val)  # now delete it

        return root

# Input: root = [5,3,6,2,4,None,7], key = 3
# Output: [5,4,6,2,None,None,7]
# One valid answer is [5,4,6,2,None,None,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,None,4,None,7] and it's also accepted.

#
# Input: root = [5,3,6,2,4,None,7], key = 0
# Output: [5,3,6,2,4,None,7]
#
# Input: root = [], key = 0
# Output: []
