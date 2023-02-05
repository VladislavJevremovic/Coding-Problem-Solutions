def has_cycle(head):
    if not head:
        return 0
    
    slowp = head
    fastp = head

    while fastp and fastp.next:
        slowp = slowp.next
        fastp = fastp.next.next
        
        if slowp == fastp:
            return 1

    return 0