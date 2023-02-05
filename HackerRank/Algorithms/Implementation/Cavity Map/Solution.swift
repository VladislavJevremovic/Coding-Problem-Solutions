func cavityMap(grid: [String]) -> [String] {
    let n = grid.count
    var result = [String]()
    for i in 0..<n {
        if i < 1 || i > n - 2 {
            result.append(grid[i])
            continue
        }

        let lineP = grid[i - 1]
        let line = grid[i]
        let lineN = grid[i + 1]

        var newLine = ""
        for j in 0..<n {
            let cv = String(line[line.index(line.startIndex, offsetBy: j)])

            if j < 1 || j > n - 2 {
                newLine += cv
                continue
            }

            let u = Int(String(lineP[lineP.index(lineP.startIndex, offsetBy: j)])) ?? 0
            let d = Int(String(lineN[lineN.index(lineN.startIndex, offsetBy: j)])) ?? 0
            let l = Int(String(line[line.index(line.startIndex, offsetBy: j - 1)])) ?? 0
            let c = Int(cv) ?? 0
            let r = Int(String(line[line.index(line.startIndex, offsetBy: j + 1)])) ?? 0

            if c > u && c > d && c > l && c > r {
                newLine += "X"
            } else {
                newLine += cv
            }
        }

        result.append(newLine)
    }

    return result
}