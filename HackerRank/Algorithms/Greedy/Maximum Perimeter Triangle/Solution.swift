func maximumPerimeterTriangle(sticks: [Int]) -> [Int] {
    let s = sticks.sorted()
    var i = sticks.count - 3
    while i >= 0 && s[i] + s[i + 1] <= s[i + 2] {
        i -= 1
    }

    return i >= 0 ? [s[i], s[i + 1], s[i + 2]] : [-1]
}