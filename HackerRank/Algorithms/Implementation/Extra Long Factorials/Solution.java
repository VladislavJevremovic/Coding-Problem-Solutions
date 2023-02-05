    static void extraLongFactorials(int n) {
        BigInteger f = BigInteger.ONE;
        for (int i = 2; i <= n; i++) 
            f = f.multiply(BigInteger.valueOf(i)); 
  
        System.out.println(f);
    }
