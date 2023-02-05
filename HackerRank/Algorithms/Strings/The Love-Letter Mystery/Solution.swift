func theLoveLetterMystery(s: String) -> Int {
    var a = Array(s)
    let n = a.count
    var r = 0
    for i in 0..<n/2 {
        let c = Int(UnicodeScalar(String(a[i]))?.value ?? 0)
        let d = Int(UnicodeScalar(String(a[n - 1 - i]))?.value ?? 0)
        r += abs(c - d)
    }
    
    return r
}