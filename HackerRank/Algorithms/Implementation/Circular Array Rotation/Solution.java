    static void rotateArrayRightOnce(int[] a) {
        int n = a.length;

        int t = a[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            a[i + 1] = a[i];
        }
        a[0] = t;
    }

    static void rotateArrayRight(int[] a, int k) {
        k = k % a.length;
        for (int i = 0; i < k; i++)
            rotateArrayRightOnce(a);
    }

    static int[] circularArrayRotation(int[] a, int k, int[] queries) {
        rotateArrayRight(a, k);

        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++)
            result[i] = a[queries[i]];

        return result;
    }
