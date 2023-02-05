static int migratoryBirds(List<Integer> arr) {
    int[] map = new int[5];
    for (Integer i: arr) {
        map[i - 1]++;
    }

    int max = 0;
    int index = -1;
    for (int i = 0; i < map.length; i++) {
        if (map[i] > max) {
            max = map[i];
            index = i;
        }
    }

    return index + 1;
}