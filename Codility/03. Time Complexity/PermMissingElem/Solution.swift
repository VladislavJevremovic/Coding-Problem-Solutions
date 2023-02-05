// https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
// Painless

public func solution(_ A : inout [Int]) -> Int {
    let N = Int64(A.count)
    var sum = (N + 1) * (N + 2) / 2
    for i in A {
        sum -= Int64(i)
    }

    return Int(sum)
}