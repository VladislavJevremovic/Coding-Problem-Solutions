func sockMerchant(n: Int, ar: [Int]) -> Int {
    var c = [Int: Int]()
    for s in ar {
        c[s] = (c[s] ?? 0) + 1
    }

    return c.values.reduce(0) { $0 + $1 / 2 }
}
