    static String timeConversion(String s) {
        String hh = s.substring(0, 2);
        if (hh.startsWith("0"))
            hh = hh.substring(1, 2);
        String rest = s.substring(2, s.length() - 2);
        String ampm = s.substring(s.length() - 2, s.length());

        Integer h = Integer.parseInt(hh);
        if (h == 12)
            h -= 12;

        if (ampm.equals("AM")) {
            return String.format("%02d", h) + rest;
        } else if (ampm.equals("PM")) {
            return String.format("%02d", (h + 12) % 24) + rest;
        } else {
            return null;
        }
    }
