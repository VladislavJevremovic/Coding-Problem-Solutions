static void printLinkedList(SinglyLinkedListNode head) {
    if (head == null)
        return;
    
    System.out.println(head.data);
    printLinkedList(head.next);
}