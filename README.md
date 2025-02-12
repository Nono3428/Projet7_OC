# Projet d'Optimisation d'Investissement en Actions

Ce projet vise à comparer deux approches pour maximiser les profits d'un investissement en actions sous contrainte de budget :

Approche de force brute - Explore toutes les combinaisons possibles pour trouver la meilleure solution.
Approche optimisée (sac à dos dynamique) - Utilise un algorithme plus efficace pour obtenir un résultat optimal en réduisant le temps de calcul.
## Installation

## Prérequis
- Python 3.x
```
https://www.python.org/
```
- Git  
```
https://git-scm.com/
```

### 1. Installation et Configuration

1. Clonez ce dépôt.    
    ```
    git clone https://github.com/Nono3428/Projet7_OC.git
    ```
2. Rendez-vous dans le répertoire du projet :  
    ```
    cd Projet7_OC
    ```

Pour utiliser ce projet, vous devez configurer l'API qui sert de backend :

1. Créez un environnement virtuel pour le projet :
    ```
    python -m venv env
    ```
2. Activez l'environnement virtuel :
    ```
    env\Scripts\activate
    ```
3. Exécuter le programme brute force :
    ```
    python brute_force.py
    ```
4. Exécuter le programme optimisé :
    ```
    python optimized.py
    ```
---

- Une fois terminer, pour désactivez l'environnement virtuel :
    ```
    env\Scripts\deactivate
    ```
---

##  Changer le fichier de données 
Si vous souhaitez tester le programme avec une autre liste d’actions, remplacez simplement le nom du fichier dans le code.

📍 Étape à suivre :
1. Ajoutez votre nouveau fichier CSV dans le dossier du projet.

2. Ouvrez le fichier Python (brute_force.py ou optimized.py).

3. Modifiez cette ligne en remplaçant "dataset.csv" par le nom de votre nouveau fichier :

**dataset = "mon_nouveau_fichier.csv"**
---