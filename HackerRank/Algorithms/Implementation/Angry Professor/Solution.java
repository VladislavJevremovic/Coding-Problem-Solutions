    static String angryProfessor(int k, int[] a) {
        int onTimeCount = 0;
        for (int i = 0; i < a.length; i++) {
            onTimeCount += (a[i] <= 0 ? 1 : 0);
        }

        return onTimeCount < k ? "YES" : "NO";
    }
