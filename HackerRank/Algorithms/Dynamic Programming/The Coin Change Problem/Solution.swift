func getWays(n: Int, c: [Int]) -> Int64 {
    var ways = [Int64](repeating: 0, count: n + 1)
    ways[0] = 1

    for i in 0..<c.count {
        if (c[i] > n) { continue }
        
        for j in c[i]...n {
            ways[j] += ways[j - c[i]]
        }
    }

    return ways[n]
}