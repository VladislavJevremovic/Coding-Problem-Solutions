func printArray(_ a: [Int]) {
    a.forEach { print(String($0) + " ", terminator: "") }
    print()
}

func insertionSort2(n: Int, arr: [Int]) {
    var a = arr

    for i in 1..<n {
        let k = a[i]

        var p = i
        while p > 0 && a[p - 1] > k {
            a[p] = a[p - 1]
            p -= 1
        }
        a[p] = k

        printArray(a)
    }
}