    static int hurdleRace(int k, int[] height) {
        int maxHeight = 0;
        for (int i = 0; i < height.length; i++) {
            if (height[i] > maxHeight)
                maxHeight = height[i];
        }

        return maxHeight <= k ? 0 : maxHeight - k;
    }
