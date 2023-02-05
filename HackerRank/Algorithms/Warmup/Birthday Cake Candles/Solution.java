    static int birthdayCakeCandles(int[] ar) {
        int max = 0;
        Map<Integer, Integer> map = new HashMap();
        for (int i = 0; i < ar.length; i++) {
            int v = ar[i];
            if (map.containsKey(v)) {
                Integer newV = map.get(v) + 1;
                map.put(v, newV);
                if (max < newV)
                    max = newV;
            } else {
                map.put(v, 1);
                if (max < 1)
                    max = 1;
            }
        }

        return max;
    }
