    static int jumpingOnClouds(int[] c) {
        int jumps = 0;
        int p = 0;
        int n = c.length;
        while (p < n) {
            if (n - 1 - p <= 2) {
                jumps++;
                break;
            } else if (c[p + 1] == 0 && c[p + 2] == 0) {
                jumps++;
                p += 2;
            } else if (c[p + 1] == 0 && c[p + 2] == 1) {
                jumps++;
                p += 1;
            } else if (c[p + 1] == 1 && c[p + 2] == 0) {
                jumps++;
                p += 2;
            } /*else if (c[p + 1] == 1 && c[p + 2] == 1) {
                jumps++;
                p += 2;
            }*/
        }

        return jumps;
    }
