static String fibonacciModified(int t1, int t2, int n) {
    BigInteger a = new BigInteger(t1 + "");
    BigInteger b = new BigInteger(t2 + "");
    for (int i = 2; i < n; i++) {
        BigInteger t = a.add(b.multiply(b));
        a = b;
        b = t;
    }

    return b.toString();
}