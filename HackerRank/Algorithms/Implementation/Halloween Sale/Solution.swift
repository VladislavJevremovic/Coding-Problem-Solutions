func howManyGames(p: Int, d: Int, m: Int, s: Int) -> Int {
    var numberOfAffordableGames = 0
    var availableFunds = s
    var currentPrice = p
    while availableFunds >= currentPrice {
        availableFunds -= currentPrice
        numberOfAffordableGames += 1
        currentPrice = max(currentPrice - d, m)
    }

    return numberOfAffordableGames
}