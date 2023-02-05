    static int findDigits(int n) {
        int result = 0;
        int m = n;
        while (m > 0) {
            int r = m % 10;
            if (r > 0)
                result += (n % r == 0 ? 1 : 0);
            m /= 10;
        }

        return result;
    }
