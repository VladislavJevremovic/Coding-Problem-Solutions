func getMinimumCost(k: Int, c: [Int]) -> Int {
    let v = c.sorted { $0 > $1 }
    
    var total = 0
    for i in 0..<v.count {
        total += ((i / k) + 1) * v[i]
    }
    
    return total
}