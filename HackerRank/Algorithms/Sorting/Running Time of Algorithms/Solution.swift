func runningTime(arr: [Int]) -> Int {
    var shifts = 0
    var a = arr

    for i in 1..<arr.count {
        let k = a[i]

        var p = i
        while p > 0 && a[p - 1] > k {
            shifts += 1
            a[p] = a[p - 1]
            p -= 1
        }

        if p != i {
            a[p] = k
        }
    }

    return shifts
}