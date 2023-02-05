static int lonelyinteger(int[] a) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < a.length; i++) {
        if (map.containsKey(a[i])) {
            map.put(a[i], map.get(a[i]) + 1);
        } else {
            map.put(a[i], 1);
        }
    }

    for (Integer i: map.keySet()) {
        if (map.get(i) == 1)
            return i;
    }

    return -1;
}