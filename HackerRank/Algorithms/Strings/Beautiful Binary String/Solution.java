static int beautifulBinaryString(String s) {
    int result = 0;
    for (int i = 0; i < s.length() - 2; i++) {
        if (s.charAt(i) == '0' &&
            s.charAt(i+1) == '1' && 
            s.charAt(i+2) == '0') {
                result++;
                i += 2;
        }
    }

    return result;
}