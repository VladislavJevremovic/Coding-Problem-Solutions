func icecreamParlor(m: Int, arr: [Int]) -> [Int] {
    var map = [Int: Int]()
    for i in 0..<arr.count {
        if arr[i] >= m {
            continue
        }

        if let v = map[arr[i]] {
            return [v + 1, i + 1]
        } else {
            map[m - arr[i]] = i
        }
    }

    return []
}