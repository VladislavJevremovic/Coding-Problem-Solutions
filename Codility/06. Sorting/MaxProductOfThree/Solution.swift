// https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
// Painless

public func solution(_ A : inout [Int]) -> Int {
    let N = A.count
    A.sort()
    return max(A[0] * A[1] * A[N - 1], A[N - 3] * A[N - 2] * A[N - 1])
}