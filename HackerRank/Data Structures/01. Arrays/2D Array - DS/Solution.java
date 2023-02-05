static int hourglassSum(int[][] a) {
    int maxSum = Integer.MIN_VALUE;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            int sum = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j + 1] + a[i + 2][j] + a[i + 2][j + 1] + a[i + 2][j + 2];

            if (sum > maxSum)
                maxSum = sum;
        }
    }

    return maxSum;
}