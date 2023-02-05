    static void plusMinus(int[] arr) {
        int n = arr.length;
        
        int pCount = 0;
        int nCount = 0;
        int zCount = 0;

        for (int i = 0; i < n; i++) {
            int v = arr[i];
            if (v < 0) {
                nCount++;
            } else if (v == 0) {
                zCount++;
            } else {
                pCount++;
            }
        }

        String pResult = String.format("%.6f", (double)pCount / n);
        String nResult = String.format("%.6f", (double)nCount / n);
        String zResult = String.format("%.6f", (double)zCount / n);

        System.out.println(pResult);
        System.out.println(nResult);
        System.out.println(zResult);
    }
