func findMedian(arr: [Int]) -> Int {
    return arr.sorted()[(arr.count - 1) / 2]
}