func stones(n: Int, a: Int, b: Int) -> [Int] {
    var r = Set<Int>()

    var d = abs(b - a)
    d = d > 0 ? d : a;
    
    var sum = min(a, b) * (n - 1)
    let maxSum = max(a, b) * (n - 1)

    while (sum <= maxSum) {
        r.insert(sum)
        sum += d
    }

    return Array(r).sorted()
}