static int pageCount(int n, int p) {
        int page1 = p / 2;
        if (n % 2 == 0)
            n++;
        int page2 = (n - p) / 2;
        
        return Math.min(page1, page2);
    }
