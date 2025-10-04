# https://leetcode.com/problems/delete-node-in-a-bst/

from typing import Optional

from python.Helpers.BinarySearchTree import BinarySearchNode, BinarySearchTree

TreeNode = BinarySearchNode


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> Optional[TreeNode]:
        """Recurse to find the key; on a two-child node replace it with its
        in-order successor (leftmost of the right subtree), then delete that."""
        # Time: O(h)   Space: O(h)   (recursion stack; h = tree height)
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


def test():
    def case(tree, key, expected_in_order):
        root = BinarySearchTree.from_level_order_sequence(tree).root if tree else None
        result = Solution().deleteNode(root, key)
        assert BinarySearchTree(result).in_order() == expected_in_order

    # delete an existing key: removed from in-order, order preserved
    case([5, 3, 6, 2, 4, None, 7], 3, [2, 4, 5, 6, 7])
    # delete a missing key: tree unchanged
    case([5, 3, 6, 2, 4, None, 7], 0, [2, 3, 4, 5, 6, 7])
    # empty tree
    case([], 0, [])

    # deterministic resulting shape for this solution's successor strategy
    root = BinarySearchTree.from_level_order_sequence([5, 3, 6, 2, 4, None, 7]).root
    result = Solution().deleteNode(root, 3)
    assert BinarySearchTree(result).to_level_order() == [5, 4, 6, 2, None, None, 7]
