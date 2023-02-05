static SinglyLinkedListNode insertNodeAtPosition(SinglyLinkedListNode head, int data, int position) {
    if (head == null) {
        head = new SinglyLinkedListNode(data);
        return head;
    } else {
        SinglyLinkedListNode seek1 = head;
        SinglyLinkedListNode seek2 = head.next;
        int seekPosition = 0;
        while (seekPosition < position - 1 && seek2 != null) {
            seek1 = seek1.next;
            seek2 = seek2.next;
            seekPosition++;
        }
        seek1.next = new SinglyLinkedListNode(data);
        seek1.next.next = seek2;

        return head;
    }
}