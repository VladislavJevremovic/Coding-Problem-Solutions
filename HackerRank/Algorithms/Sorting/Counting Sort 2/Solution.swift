func countingSort(arr: [Int]) -> [Int] {
    var c = [Int](repeating: 0, count: 100)
    for i in arr {
        c[i] += 1
    }

    var r = [Int]()
    for i in 0..<c.count {
        for _ in 0..<c[i] {
            r.append(i)
        }
    }

    return r
}