static String catAndMouse(int x, int y, int z) {
        int diffA = Math.abs(x - z);
        int diffB = Math.abs(y - z);
        if (diffA < diffB)
            return "Cat A";
        else if (diffB < diffA)
            return "Cat B";
        else
            return "Mouse C";
    }
