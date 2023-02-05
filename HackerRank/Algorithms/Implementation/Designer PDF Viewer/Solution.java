static int designerPdfViewer(int[] h, String word) {
        int wl = word.length();
        int maxHeight = 0;
        for (int i = 0; i < wl; i++) {
            char c = word.charAt(i);
            int index = c - 'a';
            if (h[index] > maxHeight)
                maxHeight = h[index];
        }

        return wl * maxHeight;
    }
