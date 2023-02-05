    static void miniMaxSum(int[] arr) {
        long min = Long.MAX_VALUE;
        long max = 0;

        long total = 0;
        for (int i = 0; i < arr.length; i++) {
            total += arr[i];
        }

        for (int i = 0; i < arr.length; i++) {
            long sum = total - arr[i];

            if (sum < min)
                min = sum;
            if (sum > max)
                max = sum;
        }

        System.out.println(min + " " + max);
    }
