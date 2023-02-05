// https://app.codility.com/programmers/lessons/16-greedy_algorithms/max_nonoverlapping_segments/
// Painless

public func solution(_ A : inout [Int], _ B : inout [Int]) -> Int {
    let N = A.count
    if N < 1 {
        return 0
    }

    var count = 1
    var end = B[0]

    for i in 1..<N {
        if A[i] > end {
            count += 1
            end = B[i]
        }
    }

    return count
}