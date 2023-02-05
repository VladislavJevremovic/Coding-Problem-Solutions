// https://app.codility.com/programmers/lessons/99-future_training/str_symmetry_point/
// Painless

public func solution(_ S : inout String) -> Int {
    let N = S.count
    if N % 2 == 0 {
        return -1
    }
    
    let M = N / 2
    let C = Array(S)
    for I in 0..<M {
        if C[I] != C[N - 1 - I] {
            return -1
        }
    }
    
    return M
}