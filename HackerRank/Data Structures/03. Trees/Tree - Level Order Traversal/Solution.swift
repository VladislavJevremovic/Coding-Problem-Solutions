func levelOrder(root: Node?) -> Void {
    var q = [Node]()

    if let root = root {
        q.insert(root, at: 0)
    }
    
    while !q.isEmpty {
        guard let n = q.popLast() else { break }
        
        print("\(n.data) ", terminator: "")

        if let left = n.left {
            q.insert(left, at: 0)
        }
        if let right = n.right {
            q.insert(right, at: 0)
        }
    }
}