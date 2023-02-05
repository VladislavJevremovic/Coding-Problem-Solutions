    static int minimumDistances(int[] a) {
        int min = Integer.MAX_VALUE;
        
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < a.length; i++) {
            if (map.containsKey(a[i])) {
                int index = map.get(a[i]);
                int d = i - index;
                if (d < min)
                    min = d;
            } else {
                map.put(a[i], i);
            }
        }

        return min < Integer.MAX_VALUE ? min : -1;
    }
