import csv

def read_actions(filename):
    """Lire les actions depuis un fichier CSV et les convertir en une liste de dictionnaires."""
    actions = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                price = float(row['price'])
                profit = float(row['profit'])
                
                if price > 0:
                    action = {
                        'name': row['name'],
                        'cost': int(price * 100),
                        'profit': profit * price / 100
                    }
                    actions.append(action)
            except ValueError:
                continue
    return actions

def knapsack(actions, budget):
    """Algorithme du sac à dos pour maximiser le profit avec un budget limité."""
    budget = int(budget * 100)
    n = len(actions)
    
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        cost = actions[i - 1]['cost']
        profit = actions[i - 1]['profit'] * 100
        
        for j in range(budget + 1):
            if cost > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + profit)
    
    selected_actions = []
    total_cost = 0
    j = budget
    
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            action_cost = actions[i - 1]['cost']
            if total_cost + action_cost <= budget:
                selected_actions.append(actions[i - 1]['name'])
                total_cost += action_cost
                j -= action_cost
    
    return dp[n][budget] / 100, selected_actions, total_cost / 100

def find_best_investment(filename, budget=500):
    """Trouve la meilleure combinaison d'actions en respectant le budget."""
    actions = read_actions(filename)
    best_profit, selected_actions, total_cost = knapsack(actions, budget)
    
    print(f"Meilleur profit possible : {best_profit:.2f} €")
    print(f"Coût total des achats : {total_cost:.2f} €")
    print("Actions achetées :")
    for action in selected_actions:
        print(f"- {action}")
    
    return best_profit, selected_actions, total_cost

dataset = 'data/dataset1.csv'
find_best_investment(dataset)