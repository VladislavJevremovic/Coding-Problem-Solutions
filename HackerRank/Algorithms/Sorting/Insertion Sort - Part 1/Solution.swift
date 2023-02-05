func printArray(_ a: [Int]) {
    a.forEach { print(String($0) + " ", terminator: "") }
    print()
}

func insertionSort1(n: Int, arr: [Int]) {
    var a = arr

    let l = a[n - 1]
    var p = n - 1
    while p > 0 && a[p - 1] > l {
        a[p] = a[p - 1]
        p -= 1

        printArray(a)
    }

    a[p] = l
    printArray(a)
}