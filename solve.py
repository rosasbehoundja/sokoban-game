"""
Ce module implémente un solveur pour le jeu Sokoban en utilisant différents algorithmes de recherche.

Les algorithmes disponibles sont:
- bfs : Recherche en largeur
- dfs : Recherche en profondeur
- astar : Recherche A* 
- gbfs : Greedy Best-First Search

Usage:
    python3 solve.py <level> <method> [--verbose]

Exemple:
    python3 solve.py 01 bfs --verbose
"""

from aima.search import breadth_first_graph_search, depth_first_graph_search, astar_search, greedy_best_first_graph_search
from Sokoban import Sokoban
from game_board import getGameBoard, print_state
import argparse
import time

def main(level:str, method:str):
    """
    Exécute le solveur Sokoban pour un niveau donné en utilisant la méthode spécifiée.
    
    Args:
        level (str): Le numéro ou identifiant du niveau à résoudre. 
        method (str): La méthode de recherche à utiliser ("bfs", "dfs", "astar", "gbfs").
    
    Returns:
        La solution trouvée

    """
    initial_agent, initial_boxes, walls, width, height, targets = getGameBoard(f"levels/sokoInst{level}.init", f"levels/sokoInst{level}.goal")
    
    print(f" --------- Initialisation de l'algorithme ---------")

    problem = Sokoban(initial=(initial_agent, initial_boxes), targets=targets, walls=walls)

    methodes_valides = ["bfs", "dfs", "astar", "gbfs"]
    if method not in methodes_valides:
        print(f"Méthode invalide. Veuillez choisir parmi: {', '.join(methodes_valides)}")
        return
    
    start_time = time.time()
    noeuds = 0 

    # Résolution
    if method == "bfs":
        print(f" - Algorithme à utiliser: Breadth-first-search\n")
        solution = breadth_first_graph_search(problem)
    elif method == "dfs":
        print(f"- Algorithme à utiliser: Depth-first-search\n")
        solution = depth_first_graph_search(problem)
    elif method == "astar":
        print(f" - Algorithme à utiliser: A* search\n")
        solution = astar_search(problem, h=problem.h)
    elif method == "gbfs":
        print(f" - Algorithme à utiliser: Greedy-best-first-search\n")
        solution = greedy_best_first_graph_search(problem, f=problem.h)

    nbre_noeuds = problem.get_explored_nodes()

    end_time = time.time() - start_time

    if solution:
        verbose = input("Afficher les états ? (0/N): ")
        if verbose.lower() == "o":
            for state in solution.path():
                print_state(state.state, walls, width=width, height=height, targets=targets)
                print()
        print(f" - Level du jeu: {level}")
        print(f"Solution trouvée avec {method} en {len(solution.path())-1} mouvements")
        print(f"Temps d'exécution: {end_time:.4f} secondes")
        print(f"Nombre de noeuds explorés : {nbre_noeuds}")
    else:
        print("Aucune solution trouvée")
        print(f"Temps d'exécution: {end_time:.4f} secondes")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Récupère le niveau de jeu et le type d'algorithme à utiliser")
    parser.add_argument("--level", required=False, help="Niveau de jeu")
    parser.add_argument("--method", required=False, help="Type d'algorithme à utiliser")

    args = parser.parse_args()
    level, method = args.level, args.method
    if level and method:
        main(level, method)
    else:
        main("01", "bfs")