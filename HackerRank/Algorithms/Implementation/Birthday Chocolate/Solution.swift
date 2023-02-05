func birthday(s: [Int], d: Int, m: Int) -> Int {
    let n = s.count
    guard m <= n else { return 0 }

    var p = [Int](repeating: 0, count: n + 1)
    for i in 1...n {
        p[i] = p[i - 1] + s[i - 1]
    }

    var r = 0
    for i in 0...n-m {
        if p[i + m] - p[i] == d {
            r += 1
        }
    }

    return r
}