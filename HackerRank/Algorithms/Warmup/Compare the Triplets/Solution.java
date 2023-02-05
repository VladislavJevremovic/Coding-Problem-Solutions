    static List<Integer> compareTriplets(List<Integer> a, List<Integer> b) {
        Integer alice = 0;
        Integer bob = 0;

        for (int i = 0; i < 3; i++) {
            int aa = a.get(i);
            int bb = b.get(i);
            if (aa > bb)
                alice++;
            else if (aa < bb)
                bob++;
        }

        List<Integer> result = new ArrayList<>();
        result.add(alice);
        result.add(bob);

        return result;
    }
