void decode(String s, Node root) {
    StringBuilder sb = new StringBuilder();

    int n = s.length();
    int p = 0;
    Node currentNode = root;
    while (p < n) {
        char c = s.charAt(p);
        p++;

        if (c == '0') {
            currentNode = currentNode.left;
        } else if (c == '1') {
            currentNode = currentNode.right;
        }

        if (currentNode.data != '\0') {
            sb.append(currentNode.data);
            currentNode = root;
        }
    }

    System.out.println(sb.toString());
}