static void bonAppetit(List<Integer> bill, int k, int b) {
        Integer sum = 0;
        for (int i = 0; i < bill.size(); i++) {
            sum += bill.get(i);
        }

        Integer sumR = sum - bill.get(k);

        Integer div = sum / 2;
        Integer divR = sumR / 2;

        if (b == divR)
            System.out.println("Bon Appetit");
        else
            System.out.println(b - divR);
    }
