static SinglyLinkedListNode deleteNode(SinglyLinkedListNode head, int position) {
    if (head == null) {
        return null;
    }

    if (position == 0) {
        return head.next;
    }

    SinglyLinkedListNode seek1 = head;
    SinglyLinkedListNode seek2 = head.next;
    int seekPosition = 0;
    while (seekPosition < position - 1 && seek2 != null) {
        seek1 = seek1.next;
        seek2 = seek2.next;
        seekPosition++;
    }
    SinglyLinkedListNode next = seek2.next;
    seek1.next = next;

    return head;
}