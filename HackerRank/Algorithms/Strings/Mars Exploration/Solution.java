static int marsExploration(String s) {
    int result = 0;
    for (int i = 0; i < s.length() - 2; i += 3) {
        if (s.charAt(i) != 'S')
            result++;
        if (s.charAt(i + 1) != 'O')
            result++;
        if (s.charAt(i + 2) != 'S')
            result++;
    }

    return result;
}