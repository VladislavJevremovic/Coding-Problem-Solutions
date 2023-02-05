func removeDuplicates(llist head: SinglyLinkedListNode?) -> SinglyLinkedListNode? {
    if head == nil || head?.next == nil {
        return head
    }
    
    if head?.data == head?.next?.data {
        head?.next = head?.next?.next
        _ = removeDuplicates(llist: head)
    } else {
        _ = removeDuplicates(llist: head?.next)
    }
    
    return head
}
