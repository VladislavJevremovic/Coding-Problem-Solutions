static long flippingBits(long n) {
    long finalResult = 0;
    for (int i = 0; i < 32; i++) {
        finalResult |= (1L << i);
    }
    
    return n ^ finalResult;
}