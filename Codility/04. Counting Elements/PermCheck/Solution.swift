// https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
// Painless

public func solution(_ A : inout [Int]) -> Int {
    let N = A.count
    var M = [Bool](repeating: false, count: N)
    for I in A {
        if I < 0 || I > N {
            return 0
        }
        if M[I - 1] {
            return 0
        }
        M[I - 1] = true
    }
    
    return 1
}