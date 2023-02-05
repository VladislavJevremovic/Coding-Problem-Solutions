static int[] gradingStudents(int[] grades) {
        int[] result = new int[grades.length];
        for (int i = 0; i < grades.length; i++) {
            int v = grades[i];
            if (v >= 38) {
                int b = 5 * ((v + 5) / 5);
                if (b - v < 3)
                    v = b;
            }

            result[i] = v;
        }

        return result;
    }
