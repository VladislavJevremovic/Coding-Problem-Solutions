boolean valuesInRange(Node root, int min, int max) {
    if (root == null)
        return true;
    
    if (root.data < min || root.data > max)
        return false;
    
    return
        valuesInRange(root.left, min, root.data - 1) && 
        valuesInRange(root.right, root.data + 1, max);
}

boolean checkBST(Node root) {
    return valuesInRange(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
}