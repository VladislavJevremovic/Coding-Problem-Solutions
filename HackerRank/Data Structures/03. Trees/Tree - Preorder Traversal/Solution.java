public static void preOrder(Node root) {
    if (root == null)
        return;
    
    System.out.print(root.data);
    System.out.print(" ");
    preOrder(root.left);
    preOrder(root.right);
}