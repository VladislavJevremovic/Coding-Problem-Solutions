static SinglyLinkedListNode insertNodeAtTail(SinglyLinkedListNode head, int data) {
    if (head == null) {
        head = new SinglyLinkedListNode(data);
        return head;
    } else {
        SinglyLinkedListNode seeker = head;
        while (seeker != null && seeker.next != null) {
            seeker = seeker.next;
        }
        seeker.next = new SinglyLinkedListNode(data);
        return head;
    }
}