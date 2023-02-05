// https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
// Respectable

public func solution(_ A : inout [Int]) -> Int {
    let N = A.count
    var M = [Int](repeating: 0, count: 100001)
    
    for I in 0..<N {
        if A[I] <= 0 {
            continue
        }
        
        M[A[I] - 1] += 1
    }
    
    for I in 0..<M.count {
        if M[I] == 0 {
            return I + 1
        }
    }
    
    return 1
}