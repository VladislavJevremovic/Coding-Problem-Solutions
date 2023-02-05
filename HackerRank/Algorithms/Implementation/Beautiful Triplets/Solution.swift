func beautifulTriplets(d: Int, a: [Int]) -> Int {    
    var map = [Int: Int]()
    for i in a {
        map[i] = (map[i] ?? 0) + 1
    }
    
    var c = 0
    for i in a {
        if (map[i + d] ?? 0 > 0) && (map[i + 2 * d] ?? 0 > 0) {
            c += 1
        }
    }

    return c
}