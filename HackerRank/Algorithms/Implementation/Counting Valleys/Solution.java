static int countingValleys(int n, String s) {
        int level = 0;
        int valleys = 0;
        boolean didNotEnterValley = true;

        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == 'U') {
                level++;
                if (level >= 0)
                    didNotEnterValley = true;
            } if (c == 'D') {
                level--;
                if (level < 0 && didNotEnterValley) {
                    valleys++;
                    didNotEnterValley = false;
                }
            }
        }

        return valleys;
    }
