static void countApplesAndOranges(int s, int t, int a, int b, int[] apples, int[] oranges) {
        int appleCount = 0;
        int orangeCount = 0;

        for (int i = 0; i < apples.length; i++) {
            int d = a + apples[i];
            appleCount += (s <= d && d <= t ? 1 : 0);
        }

        for (int i = 0; i < oranges.length; i++) {
            int d = b + oranges[i];
            orangeCount += (s <= d && d <= t ? 1 : 0);
        }

        System.out.println(appleCount);
        System.out.println(orangeCount);
    }
