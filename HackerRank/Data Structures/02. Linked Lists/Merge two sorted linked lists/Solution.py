def mergeLists(head1, head2):
    dummy_head = SinglyLinkedListNode(0)
    merged_so_far = dummy_head

    while head1 is not None or head2 is not None:
        if head1 is None:
            merged_so_far.next = head2
            break
        elif head2 is None:
            merged_so_far.next = head1
            break
        else:
            if head1.data < head2.data:
                merged_so_far.next = head1
                head1 = head1.next
            else:
                merged_so_far.next = head2
                head2 = head2.next
        merged_so_far = merged_so_far.next

    return dummy_head.next