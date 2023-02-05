    static int surfaceArea(int[][] A) {
        int area = 0;
        
        int rows = A.length;
        int columns = A[0].length;
        
        int t, b, u, d, l, r;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                t = b = u = d = l = r = 0;
                
                int v = A[i][j];
                
                if (v > 0) {
                    t++;
                    b++;
                }
                
                // UP
                if (i >= 1) {
                    if (v > A[i-1][j])
                        u = v - A[i-1][j];
                } else
                    u = v;
                
                // DOWN
                if (i < rows - 1) {
                    if (v > A[i+1][j])
                        d = v - A[i+1][j];
                } else
                    d = v;
                
                // LEFT
                if (j >= 1) {
                    if (v > A[i][j-1])
                        l = v - A[i][j-1];
                } else
                    l = v;
                
                // RIGHT
                if (j < columns - 1) {
                    if (v > A[i][j+1])
                        r = v - A[i][j+1];
                } else
                    r = v;
                
                area = area + t + b + u + d + l + r;  
            }
        }
        
        return area;
    }
