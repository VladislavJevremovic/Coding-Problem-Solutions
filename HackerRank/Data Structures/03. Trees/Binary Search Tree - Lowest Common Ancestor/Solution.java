public static Node lca(Node root, int v1, int v2) {
  	Queue<Node> q = new LinkedList();
    if (root != null)
        q.add(root);

    if (v1 > v2) {
        int t = v1;
        v1 = v2;
        v2 = t;
    }

    while (!q.isEmpty()) {
        Node n = q.remove();
        if (v1 <= n.data && n.data <= v2)
            return n;

        if (n.left != null)
            q.add(n.left);
        if (n.right != null)
            q.add(n.right);
    }

    return null;
}

public static Node lca(Node root, int v1,int v2) {
    if (root.data < v1 && root.data < v2) {
        return lca(root.right, v1, v2);
    }
    
    if (root.data > v1 && root.data > v2) {
        return lca(root.left, v1, v2);
    }

    return root;
}