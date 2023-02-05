func equalizeArray(arr: [Int]) -> Int {
    var max = 1
    var map: [Int: Int] = [:]
    for i in arr {
        if let v = map[i] {
            let newV = v + 1
            map[i] = newV

            if newV > max {
                max = newV
            }
        } else {
            map[i] = 1
        }
    }

    return arr.count - max
}
