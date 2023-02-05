static int getNode(SinglyLinkedListNode head, int positionFromTail) {
    int n = 0;
    SinglyLinkedListNode counter = head;
    while (counter != null) {
        n++;
        counter = counter.next;
    }

    SinglyLinkedListNode runner = head;

    int remainingShifts = n - 1 - positionFromTail;
    while (runner != null && remainingShifts > 0) {
        runner = runner.next;
        remainingShifts--;
    }

    return runner.data;
}