// https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
// Painless

public func solution(_ A : inout [Int], _ K : Int) -> [Int] {
    let N = A.count
    if N == 0 {
        return A
    }

    let k = K % N
    if k > 0 {
        for _ in 1...k {
            let temp = A[N - 1]
            for j in (0...N - 2).reversed() {
                A[j + 1] = A[j]
            }
            A[0] = temp
        }
    }

    return A
}