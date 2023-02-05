func findLonely(arr: [Int]) -> Int {
    var value = 0
    for i in arr {
        value ^= i
    }
    
    return value
}