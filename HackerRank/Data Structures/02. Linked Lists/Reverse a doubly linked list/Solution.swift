func reverse(llist head: DoublyLinkedListNode?) -> DoublyLinkedListNode? {
    let temp = head?.next
    head?.next = head?.prev
    head?.prev = temp
    return temp == nil ? head : reverse(llist: temp)
}