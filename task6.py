def greedy_algorithm(items, budget):
    res = []
    items = sorted(items.values(), key=lambda x: x["cost"] / x["calories"], reverse=True)
    for item in items:
        if item["cost"] <= budget:
            budget -= item["cost"]
            res.append(item)
    return res

def dynamic_programming(items, budget):
    products = list(items.keys())
    costs = [items[name]['cost'] for name in products]
    calories = [items[name]['calories'] for name in products]

    n = len(products)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(budget + 1):
            if costs[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    j = budget
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(items[products[i - 1]])
            j -= costs[i - 1]
    
    return selected_items

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}    

print('Greedy algorithm:')
print(greedy_algorithm(items, 100))
print('Dynamic programming:')
print(dynamic_programming(items, 100))