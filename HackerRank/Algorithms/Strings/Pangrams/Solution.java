static String pangrams(String s) {
    int[] letters = new int[26];

    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if ('a' <= c && c <= 'z') {
            letters[c - 'a']++;
        } else if ('A' <= c && c <= 'Z') {
            letters[c - 'A']++;
        }
    }

    boolean result = true;
    for (int i = 0; i < letters.length; i++) {
        if (letters[i] < 1) {
            result = false;
            break;
        }
    }

    return result ? "pangram" : "not pangram";
}