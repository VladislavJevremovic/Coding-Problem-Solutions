static int[] breakingRecords(int[] scores) {
        int[] result = new int[2];

        int highest = 0;
        int lowest = Integer.MAX_VALUE;
        for (int i = 0; i < scores.length; i++) {
            int v = scores[i];
            if (v > highest) {
                highest = v;
                if (i > 0) {
                    result[0]++;
                }
            }
            if (v < lowest) {
                lowest = v;
                if (i > 0) {
                    result[1]++;
                }
            }
        }

        return result;
    }
