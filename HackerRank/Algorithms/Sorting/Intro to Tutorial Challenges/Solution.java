static int introTutorial(int V, int[] arr) {
    int a = 0;
    int b = arr.length - 1;
    while (a <= b) {
        int p = (a + b) / 2;
        
        if (arr[p] == V) {
            return p;
        } else if (arr[p] < V) {
            a = p + 1;
        } else {
            b = p - 1;
        }
    }

    return -1;
}