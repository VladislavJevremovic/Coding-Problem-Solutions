    static int[] permutationEquation(int[] p) {
        int n = p.length;
        int[] result = new int[n];

        Map<Integer, Integer> sequenceFunction = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            sequenceFunction.put(p[i - 1], i);
        }
        
        for (int i = 1; i <= n; i++) {
            result[i - 1] = sequenceFunction.get(sequenceFunction.get(i));
        }

        return result;
    }
