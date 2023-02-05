static int camelcase(String s) {
    int r = 1;
    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if ('A' <= c && c <= 'Z')
            r++;
    }
        
    return r;
}