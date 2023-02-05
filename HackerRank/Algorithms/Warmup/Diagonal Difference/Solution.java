    static int diagonalDifference(int[][] arr) {
        int sum1 = 0;
        int sum2 = 0;

        for (int i = 0; i < arr.length; i++) {
            sum1 += arr[i][i];
            sum2 += arr[i][arr.length - 1 - i];
        }

        return Math.abs(sum1 - sum2);
    }
