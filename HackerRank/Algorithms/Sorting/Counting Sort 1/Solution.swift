func countingSort(arr: [Int]) -> [Int] {
    var c = [Int](repeating: 0, count: 100)
    for i in arr {
        c[i] += 1
    }

    return c
}