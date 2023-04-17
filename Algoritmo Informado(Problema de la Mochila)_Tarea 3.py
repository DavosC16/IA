from queue import PriorityQueue

class Item:
    def __init__(self, weight, value):
        self.value = value
        self.weight = weight
        self.cost = value / weight

    def __lt__(self, other):
        return self.cost < other.cost

def knapsack(items, capacity):
    items = sorted(items, reverse=True)
    queue = PriorityQueue()
    queue.put((0, 0, 0))
    max_profit = 0

    while not queue.empty():
        profit, weight, level = queue.get()

        if level == len(items):
            if profit > max_profit:
                max_profit = profit
            continue

        item = items[level]

        if weight + item.weight <= capacity:
            queue.put((
                profit + item.value,
                weight + item.weight,
                level + 1
            ))

        bound = profit + (capacity - weight) * item.cost
        if bound > max_profit:
            queue.put((profit, weight, level + 1))

    return max_profit

#vi wi
items = [
    Item(95, 55),
    Item(4, 10),
    Item(60, 47),
    Item(32, 5),
    Item(23, 4),
    Item(72, 50),
    Item(80, 8),
    Item(62, 61),
    Item(65, 85),
    Item(46, 87)
]

capacity = 269

max_profit = knapsack(items, capacity)

print("Optimo:", max_profit)

