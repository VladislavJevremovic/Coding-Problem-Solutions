static boolean isLeapYear(int year) {
        boolean julian = (year % 4 == 0);
        boolean gregorian = (year % 400 == 0 || ((year % 4 == 0) && (year % 100 != 0)));

        return year < 1919 ? julian : gregorian;
    }

    static String dayOfProgrammer(int year) {
        int day = isLeapYear(year) ? 12 : 13;
        if (year == 1918) {
            return String.format("26.09.%d", year);
        }
        return String.format("%d.09.%d", day, year);
    }
