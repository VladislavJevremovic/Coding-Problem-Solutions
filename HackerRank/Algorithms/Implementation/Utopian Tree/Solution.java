    static int utopianTree(int n) {
        int height = 1;
        int rem = n % 2;
        int yearCycles = n / 2;
        
        for (int i = 0; i < yearCycles; i++) {
            height *= 2;
            height += 1;
        }

        if (rem > 0)
            height *= 2;

        return height;
    }
