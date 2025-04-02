from aima.search import Problem
from game_board import getGameBoard, print_state

class Sokoban(Problem):

    def __init__(self, initial, targets, walls):
        super().__init__(initial)
        self.initial = initial
        self.targets = targets
        self.walls = walls
        self.sequences = []

    def actions(self, state):
        """
        Take the state and returns the actions that can be executed.
        """
        directions = [('Up', (0, -1)), ('Down', (0, 1)), ('Left', (-1, 0)), ('Right', (1, 0))]
        valid_actions = [] # liste des actions valides
        agent, boxes = state # position de l'agent & des boxes

        for action, (dx, dy) in directions:
            new_x = agent[0] + dx
            new_y = agent[1] + dy

            # Vérifier les collisions
            if (new_x, new_y) in self.walls:
                continue

            # Vérifier si l'agent se déplace vers un box
            if (new_x, new_y) in boxes:
                new_box_x = new_x + dx
                new_box_y = new_y + dy

                if (new_box_x, new_box_y) not in self.walls and (new_box_x, new_box_y) not in boxes:
                    valid_actions.append(action)
            else:
                valid_actions.append(action)
        return valid_actions

    def result(self, state, action):
        """
        Update state
        """
        directions = {
            'Up': (0, -1),
            'Down': (0, 1),
            'Left': (-1, 0),
            'Right': (1, 0)
        }
        agent, boxes = state
        dx, dy = directions[action]

        new_agent = (agent[0] + dx, agent[1] + dy)
        new_boxes = set(boxes)

        if new_agent in new_boxes:
            # pousser la boite
            new_box = (new_agent[0] + dx, new_agent[1] + dy)
            new_boxes.remove(new_agent)
            new_boxes.add(new_box)

        return (new_agent, frozenset(new_boxes))
    
    def is_dead_state(self, boxes):
        """Vérifie si les boites se retrouvent dans des angles morts"""
        for box in boxes:
            if box not in self.targets:
                x, y = box
                # Vérifier si la boîte est dans un coin
                left_wall = (x-1, y) in self.walls
                right_wall = (x+1, y) in self.walls
                up_wall = (x, y-1) in self.walls
                down_wall = (x, y+1) in self.walls
                if (left_wall or right_wall) and (up_wall or down_wall):
                    return True
        return False

    def goal_test(self, state):
        """
        Tell us if we reach the goal state
        """
        _, boxes = state
        return all(box in self.targets for box in boxes)
    
    def heuristic(self, node):
        """Fonction heuristique pour les algorithmes de recherche informée"""
        total = 0
        for box in node.state[1]:
            if box not in self.targets:
                min_dist = min(abs(box[0] - t[0]) + abs(box[1] - t[1]) for t in self.targets)
                total += min_dist
        return total
    
    def path_cost(self, c, state1, action, state2):
        """
        Return cost of path from state1 to state2 given action
        """
        return c + 1
    

if __name__ == "__main__":
    from aima.search import astar_search, greedy_best_first_graph_search

    initial_agent, initial_boxes, walls, width, height, targets = getGameBoard("levels/sokoInst02.init", "levels/sokoInst02.goal")
    # Initialisation
    problem = Sokoban(initial=(initial_agent, initial_boxes), targets=targets, walls=walls)

    # Résolution avec A*
    print(">> A*")
    solution = astar_search(problem, h= problem.heuristic, display= True)
    # print(">> GBS")
    # solution = greedy_best_first_graph_search(problem, f = problem.heuristic, display=True)
    if solution:
        for state in solution.path():
            print_state(state.state, walls, width=width, height=height, targets=targets)
            print()