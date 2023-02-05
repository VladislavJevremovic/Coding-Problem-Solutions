static String funnyString(String s) {
    int n = s.length();
    
    char[] rc = s.toCharArray();
    for (int i = 0; i < n / 2; i++) {
        char t = rc[i];
        rc[i] = rc[n - 1 - i];
        rc[n - 1 - i] = t;
    }
    String r = new String(rc);

    
    boolean funny = true;
    for (int i = 0; i < s.length() - 1; i++) {
        int d1 = Math.abs(s.charAt(i + 1) - s.charAt(i));
        int d2 = Math.abs(r.charAt(i + 1) - r.charAt(i));
        if (d1 != d2) {
            funny = false;
            break;
        }
    }
    return funny ? "Funny" : "Not Funny";
}