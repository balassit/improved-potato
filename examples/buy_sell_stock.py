from typing import List


def buy_and_sell_stock_k_times(prices: List[float], k: int):
    if k == 0:
        return 0
    if 2 ** k >= len(prices):
        return sum(max(0.0, b - a) for a, b in zip(prices[:-1], prices[1:]))

    min_prices, max_profits = [float("inf")] * k, [0.0] * k
    for price in prices:
        for i in reversed(range(k)):
            max_profits[i] = max(max_profits[i], price - min_prices[i])
            min_prices[i] = min(min_prices[i], price - (0 if i == 0 else max_profits[i - 1]))
    return max_profits[-1]


if __name__ == "__main__":
    res = buy_and_sell_stock_k_times(
        [225, 220, 230, 245, 235, 230, 250, 260, 210, 200, 245, 255, 240], 3
    )
    print(res)
