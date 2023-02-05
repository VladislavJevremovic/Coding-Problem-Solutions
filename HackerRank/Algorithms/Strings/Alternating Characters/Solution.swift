func alternatingCharacters(s: String) -> Int {
    let a = Array(s)
    var c = 0
    for j in 0..<a.count - 1 {
        if a[j] == a[j + 1] {
            c += 1
        }
    }

    return c
}