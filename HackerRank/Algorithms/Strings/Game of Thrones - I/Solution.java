static String gameOfThrones(String s) {
    int[] cf = new int[26];
    for (int i = 0; i < s.length(); i++) {
        cf[s.charAt(i) - 'a']++;
    }

    int odds = 0;
    for (int i = 0; i < cf.length; i++) {
        if (cf[i] % 2 > 0)
            odds++;
    }

    return odds <= 1 ? "YES" : "NO";
}