// https://app.codility.com/programmers/lessons/6-sorting/triangle/
// Painless

public func solution(_ A : inout [Int]) -> Int {
    let N = A.count
    if N < 3 {
        return 0
    }

    A.sort()

    for i in 0..<N - 2 {
        if A[i] + A[i + 1] > A[i + 2] {
            return 1
        }
    }

    return 0
}