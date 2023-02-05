    static int[] serviceLane(int[] width, int n, int[][] cases) {
        int[] result = new int[cases.length];
        for (int i = 0; i < cases.length; i++) {
            int min = Integer.MAX_VALUE;
            int a = cases[i][0];
            int b = cases[i][1];
            for (int j = a; j <= b; j++) {
                if (width[j] < min)
                    min = width[j];
            }

            result[i] = min;
        }

        return result;
    }
