def knapsack(items, capacity):
    def busqueda(current_weight, current_value, i):
        nonlocal max_profit
        if current_weight > capacity:
            return
        if current_value > max_profit:
            max_profit = current_value
        if i >= len(items):
            return
        busqueda(current_weight + items[i][0], current_value + items[i][1], i + 1)
        busqueda(current_weight, current_value, i + 1)

    max_profit = 0
    busqueda(0, 0, 0)
    return max_profit

items = [
    (95, 55),
    (4, 10),
    (60, 47),
    (32, 5),
    (23, 4),
    (72, 50),
    (80, 8),
    (62, 61),
    (65, 85),
    (46, 87)
]

capacity = 269

max_profit = knapsack(items, capacity)

print("Optimo = ", max_profit)