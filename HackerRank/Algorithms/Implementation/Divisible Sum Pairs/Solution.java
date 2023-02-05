static int divisibleSumPairs(int n, int k, int[] ar) {
        int sum = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (i == j)
                    continue;
                if ((ar[i] + ar[j]) % k == 0)
                    sum++;
            }
        }

        return sum;
    }
