func fairRations(b: [Int]) -> String {
    let n = b.count
    var r = 0
    var c = 0

    for i in 0..<n {
        let p = b[i] + c
        if p % 2 == 1 {
            if i == n - 1 {
                return "NO"
            } else {
                r += 2
                c = 1
            }
        } else {
            c = 0
        }
    }

    return String(r)
}