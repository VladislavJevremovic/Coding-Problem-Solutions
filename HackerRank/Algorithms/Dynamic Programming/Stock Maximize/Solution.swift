func stockmax(prices: [Int]) -> Int64 {
    var profit = Int64(0)
    var maxSoFar = 0
    var i = prices.count - 1
    while i >= 0 {
        if prices[i] >= maxSoFar {
            maxSoFar = prices[i]
        }
        profit += Int64(maxSoFar - prices[i])
        
        i -= 1
    }
    
    return profit
}