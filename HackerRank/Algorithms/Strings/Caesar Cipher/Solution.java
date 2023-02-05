static String caesarCipher(String s, int k) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        
        if ('a' <= c && c <= 'z') {
            c = (char)('a' + (c - 'a' + k % 26) % 26);
        } else if ('A' <= c && c <= 'Z') {
            c = (char)('A' + (c - 'A' + k % 26) % 26);
        }

        sb.append(String.valueOf(c));
    }

    return sb.toString();
}