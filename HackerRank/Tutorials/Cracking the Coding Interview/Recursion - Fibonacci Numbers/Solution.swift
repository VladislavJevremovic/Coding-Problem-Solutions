import Foundation

func fibonacci (n: Int) -> Int {
    if n < 2 {
        return n
    }
    
    var n_2 = 0 // n - 2
    var n_1 = 1 // n - 1
    for _ in 0..<n-1 {
        let t = n_1 + n_2
        n_2 = n_1
        n_1 = t
    }

    return n_1
}

// read the integer n
let n = Int(readLine()!)!

// print the nth fibonacci number
print(fibonacci(n: n))
