// https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
// Painless

public func solution(_ A : inout [Int]) -> Int {
    let n = A.count
    let total = A.reduce(0, +)
    
    var result = Int.max
    var first = 0
    
    for i in 0..<n-1 {
        first += A[i]
        
        let second = total - first
        let diff = abs(first - second)
        result = min(result, diff)
    }

    return result
}