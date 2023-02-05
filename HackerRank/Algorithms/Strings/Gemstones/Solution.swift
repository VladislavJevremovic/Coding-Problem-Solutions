func gemstones(arr: [String]) -> Int {
    var result = 0
    
    let alphabet = "abcdefghijklmnopqrstuvwxyz"
    for c in alphabet {
        var ok = true
        for s in arr {
            if !s.contains(c) {
                ok = false
                break
            }
        }
        
        result += ok ? 1 : 0
    }

    return result
}