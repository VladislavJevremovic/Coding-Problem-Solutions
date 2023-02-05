func cutTheSticks(arr: [Int]) -> [Int] {
    var result = [Int]()
    
    var sarr = arr.sorted { $0 > $1 }
    while (!sarr.isEmpty) {
        result.append(sarr.count)
        
        let last = sarr.last ?? 0
        sarr = sarr.compactMap { $0 > last ? $0 - last : nil }
    }
    
    return result
}