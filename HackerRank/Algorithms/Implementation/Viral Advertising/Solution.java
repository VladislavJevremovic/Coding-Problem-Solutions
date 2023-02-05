    static int viralAdvertising(int n) {
        int cseen = 5;
        int sum = 0;
        
        int i = 1;
        while (i <= n) {
            int a = cseen / 2;

            sum += a;
            cseen = a * 3;

            i++;
        }

        return sum;
    }
