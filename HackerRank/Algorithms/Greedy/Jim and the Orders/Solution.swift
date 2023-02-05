typealias Order = (orderTime: Int, index: Int)

func jimOrders(orders: [[Int]]) -> [Int] {
    var orderMap = [Order]()
    for i in 0..<orders.count {
        orderMap.append((orders[i][0] + orders[i][1], i + 1))
    }
    orderMap.sort { $0.orderTime < $1.orderTime }

    return orderMap.map { $0.index }
}