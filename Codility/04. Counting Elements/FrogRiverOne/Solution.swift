// https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
// Painless

public func solution(_ X : Int, _ A : inout [Int]) -> Int {
    var M = [Bool](repeating: false, count: X)

    var R = -1
    var S = 0
    
    var I = 0
    while I < A.count && R < 0 {
        let K = A[I] - 1
        if !M[K] {
            M[K] = true
            S += 1
        }

        if S == X {
            R = I
        }

        I += 1
    }

    return R
}