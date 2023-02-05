static int anagram(String s) {
    int[] lettersArray = new int[26];
    if (s.length() % 2 == 0) {
        for (int j = 0; j < s.length() / 2; j++){
            lettersArray[s.charAt(j) - 'a']++;
        }
        for (int j = s.length() / 2; j < s.length(); j++) {
            lettersArray[s.charAt(j) - 'a']--;
        }

        int changes = 0;
        for (int j = 0; j < lettersArray.length; j++) {
            changes += Math.abs(lettersArray[j]);
        }
        
        return changes / 2;
    } else{
        return -1;
    }
}