func maximizingXor(l: Int, r: Int) -> Int {
    var max = 0
    for i in l...r {
        for j in l...r where i <= j {
            let x = i ^ j
            if x > max {
                max = x
            }
        }
    }

    return max
}