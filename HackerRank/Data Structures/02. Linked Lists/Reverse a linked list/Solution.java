static SinglyLinkedListNode reverse(SinglyLinkedListNode head) {
    SinglyLinkedListNode tail;
    while (head != null) {
        SinglyLinkedListNode t = head->next;
        head->next = tail;
        tail = head;
        head = t;
    }
    
    return tail;
}

func reverse(llist head: SinglyLinkedListNode?) -> SinglyLinkedListNode? {
    var tail: SinglyLinkedListNode? = nil
    var headR = head
    while (headR != nil) {
        let t = headR?.next
        headR?.next = tail
        tail = headR
        headR = t
    }
    
    return tail
}
