func getMoneySpent(keyboards: [Int], drives: [Int], b: Int) -> Int {
    var max = -1
    for i in 0..<keyboards.count {
        for j in 0..<drives.count {
            let s = keyboards[i] + drives[j]
            if s <= b && s > max {
                max = s
            }
        }
    }

    return max
}
