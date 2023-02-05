// https://app.codility.com/programmers/lessons/6-sorting/distinct/
// Painless

public func solution(_ A : inout [Int]) -> Int {
    A.sort()

    let N = A.count
    var C = 0

    if N > 0 {
        C += 1
        for I in 0..<N - 1 {
            if A[I] != A[I + 1] {
                C += 1
            }
        }
    }

    return C
}