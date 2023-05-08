import random

def grasp_knapsack(values, weights, capacity, max_iterations):
    n = len(values)
    best_solution = None
    best_value = 0
    
    for _ in range(max_iterations):
        current_solution = [0] * n
        current_value = 0
        current_weight = 0
        
        while current_weight < capacity:
            candidate_items = []
            for i in range(n):
                if current_solution[i] == 0 and current_weight + weights[i] <= capacity:
                    candidate_items.append(i)
            
            if not candidate_items:
                break
            
            item = random.choice(candidate_items)
            current_solution[item] = 1
            current_value += values[item]
            current_weight += weights[item]
        
        if current_value > best_value:
            best_solution = current_solution
            best_value = current_value
    
    return best_solution, best_value
