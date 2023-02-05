// https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
// Respectable

public func solution(_ N : Int, _ A : inout [Int]) -> [Int] {
    let M = A.count
    var R = [Int](repeating: 0, count: N)

    var MAX_VALUE = 0
    var LAST_MAX_VALUE = 0

    for I in 0..<M {
        if A[I] <= N {
            R[A[I] - 1] = max(R[A[I] - 1], LAST_MAX_VALUE)
            R[A[I] - 1] += 1
            MAX_VALUE = max(MAX_VALUE, R[A[I] - 1])
        } else {
            LAST_MAX_VALUE = MAX_VALUE
        }
    }

    if LAST_MAX_VALUE > 0 {
        for I in 0..<N {
            R[I] = max(R[I], LAST_MAX_VALUE)
        }
    }

    return R
}