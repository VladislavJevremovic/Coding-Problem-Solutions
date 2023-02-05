static int squares(int a, int b) {
    int aa = (int) Math.floor(Math.sqrt(a));
    int bb = (int) Math.ceil(Math.sqrt(b));
    int c = 0;
    for (int i = aa; i <= bb; i++) {
        if (a <= i * i && i * i <= b)
            c++;
    }
    
    return c;
}