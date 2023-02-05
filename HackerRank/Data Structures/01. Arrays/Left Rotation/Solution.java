public static void rotateLeftByOne(int[] a) {
    int n = a.length;
    int t = a[0];
    for (int i = 1; i < a.length; i++) {
        a[i - 1] = a[i];
    }
    a[n - 1] = t;
}

public static void rotateLeft(int[] a, int d) {
    for (int i = 0; i < d; i++) {
        rotateLeftByOne(a);
    }
}