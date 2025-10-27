def greedy_kapsack(weights, profits, capacity):
    n = len(weights)
    ratios = [(profits[i] / weights[i], weights[i], profits[i], i) for i in range(n)]
    ratios.sort(reverse=True, key=lambda x: x[0])
    
    total_profit = 0
    total_weight = 0
    fractions = [0] * n
    
    for ratio, weight, profit, indx in ratios:
        if total_weight + weight <= capacity:
            fractions[indx] = 1
            total_weight += weight
            total_profit += profit
        else:
            remaining_capacity = capacity - total_weight
            fraction = remaining_capacity / weight
            fractions[indx] = fraction
            total_weight += weight * fraction
            total_profit += profit * fraction
            break  
    
    return total_profit, total_weight, fractions

m = int(input("Enter number of items: "))
weights = []
profits = []

for i in range(m):
    w = float(input(f"Enter weight of item {i + 1}: "))
    p = float(input(f"Enter profit of item {i + 1}: "))
    weights.append(w)
    profits.append(p)

capacity = float(input("Enter capacity: "))

total_profit, total_weight, fractions = greedy_kapsack(weights, profits, capacity)
print("Total profit:", total_profit)
print("Total weight:", total_weight)
print("Fractions of items taken:", fractions)




print(f"Total profit: {profit}\nFractions: {frac}")
