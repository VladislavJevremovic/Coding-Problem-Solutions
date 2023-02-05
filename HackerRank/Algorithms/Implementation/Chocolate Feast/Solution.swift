func chocolateFeast(n: Int, c: Int, m: Int) -> Int {
    var b = n / c
    var l = 0
    
    var s = b
    var t = b + l
    while t >= m {
        b = t / m
        l = t % m
        
        s += b
        t = b + l
    }

    return s
}