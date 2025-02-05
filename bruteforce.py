import csv

def read_actions(filename):
    """Lire les actions depuis un fichier CSV et les stocker sous forme de liste de dictionnaires."""
    actions = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            action = {
                'name': row['Actions #'],
                'cost': int(row['Coût par action (en euros)']),
                'profit_percent': float(row['Bénéfice (après 2 ans)'].strip('%'))
            }
            actions.append(action)
    return actions

def calculate_profit(combination):
    """Calculer le profit total d'une combinaison d'actions."""
    total_profit = 0
    for action in combination:
        total_profit += action['cost'] * (action['profit_percent'] / 100)
    return total_profit

def find_best_investment_recursive(actions, index=0, current_combination=[], best_combination=[], best_profit=0, budget=500):
    """Fonction récursive pour explorer toutes les combinaisons possibles et trouver le meilleur investissement."""
    
    # Calcul du coût actuel de la combinaison
    total_cost = sum(action['cost'] for action in current_combination)

    # Si le coût dépasse le budget, on arrête cette branche de recherche
    if total_cost > budget:
        return best_combination, best_profit

    # Calcul du profit actuel
    current_profit = calculate_profit(current_combination)

    # Si on trouve une meilleure combinaison, on la sauvegarde
    if current_profit > best_profit:
        best_combination = list(current_combination)
        best_profit = current_profit

    # Si on a exploré toutes les actions, on retourne la meilleure combinaison trouvée
    if index >= len(actions):
        return best_combination, best_profit

    # 1️⃣ Cas où on **n'ajoute pas** l'action actuelle et on passe à la suivante
    best_combination, best_profit = find_best_investment_recursive(
        actions, index + 1, current_combination, best_combination, best_profit, budget
    )

    # 2️⃣ Cas où on **ajoute** l'action actuelle et on continue la recherche
    current_combination.append(actions[index])
    best_combination, best_profit = find_best_investment_recursive(
        actions, index + 1, current_combination, best_combination, best_profit, budget
    )

    # Retirer l'élément ajouté pour revenir à l'état précédent (backtracking)
    current_combination.pop()

    return best_combination, best_profit

# Charger les actions depuis le fichier CSV
filename = 'actions.csv'  # Assurez-vous que le fichier CSV est bien dans le bon chemin
actions = read_actions(filename)

# Trouver la meilleure combinaison d'investissement avec la version brute-force sans itertools
best_combination, best_profit = find_best_investment_recursive(actions)

# Affichage du résultat
print(f"Meilleur investissement : {[action['name'] for action in best_combination]}")
print(f"Coût total : {sum(action['cost'] for action in best_combination)} €")
print(f"Profit total : {best_profit} €")
