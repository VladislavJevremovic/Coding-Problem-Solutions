func sortedInsert(llist head: DoublyLinkedListNode?, data: Int) -> DoublyLinkedListNode? {
    let newNode = DoublyLinkedListNode(nodeData: data)
    guard let head = head else {
        return newNode
    }
    if data <= head.data {
        newNode.next = head
        head.prev = newNode
        return newNode
    } else {
        let rest = sortedInsert(llist: head.next, data: data)
        head.next = rest
        rest?.prev = head
        return head
    }
}