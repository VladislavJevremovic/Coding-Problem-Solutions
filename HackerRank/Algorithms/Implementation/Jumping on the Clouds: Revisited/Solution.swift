func jumpingOnClouds(c: [Int], k: Int) -> Int {
    var e = 100
    var i = 0
    repeat {
        i = (i + k) % c.count
        e -= 1
        if c[i] == 1 {
            e -= 2
        }
    } while i != 0

    return e
}