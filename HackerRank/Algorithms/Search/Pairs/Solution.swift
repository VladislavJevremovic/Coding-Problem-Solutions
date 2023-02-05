func pairs(k: Int, arr: [Int]) -> Int {
    let a = arr.sorted()
    var i = 0
    var j = 1
    var c = 0
    while j < a.count {
        var d = a[j] - a[i]
        if d == k {
            c += 1
            j += 1
        } else if d > k {
            i += 1
        } else if d < k {
            j += 1
        }
    }

    return c
}