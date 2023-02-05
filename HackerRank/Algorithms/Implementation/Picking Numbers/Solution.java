public static int pickingNumbers(List<Integer> a) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int i = 0; i < a.size(); i++) {
            int num = a.get(i);
            if (freq.containsKey(num))
                freq.put(num, freq.get(num) + 1);
            else
                freq.put(num, 1);
        }

        int max = 0;
        for (int i : freq.keySet()) {
            int left = (freq.containsKey(i - 1)) ? freq.get(i) + freq.get(i - 1) : freq.get(i);
            int right = (freq.containsKey(i + 1)) ? freq.get(i) + freq.get(i + 1) : freq.get(i);
            
            if (left > max)
                max = left;
            if (right > max)
                max = right;
        }

        return max;
    }
