# https://leetcode.com/problems/delete-node-in-a-linked-list/

class Solution:
    def deleteNode(self, node):
        processed_node = None
        while node and node.next:
            node.val = node.next.val
            processed_node = node
            node = node.next
        processed_node.next = None

# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
#
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
#
# Input: head = [1,2,3,4], node = 3
# Output: [1,2,4]
#
# Input: head = [0,1], node = 0
# Output: [1]
#
# Input: head = [-3,5,-99], node = -3
# Output: [5,-99]
