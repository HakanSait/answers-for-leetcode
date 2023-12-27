function buyChoco (prices: number[], money: number): number {
    prices.sort((a, b) => a - b);

    const minimumPrice: number = prices[0] + prices[1];

    if (minimumPrice > money) {
        return money;
    } else {
        return money - minimumPrice;
    }
}
