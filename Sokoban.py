from aima.search import Problem
from heuristics import manhattan_distance, greedy_matching_distance

class Sokoban(Problem):

    def __init__(self, initial, targets, walls, heuristic_type='manhattan'):
        super().__init__(initial)
        self.initial = initial
        self.targets = targets
        self.walls = walls
        self.explored_nodes = 0
        self.heuristic_type = heuristic_type

    def actions(self, state):
        directions = [('Up', (0, -1)), ('Down', (0, 1)), ('Left', (-1, 0)), ('Right', (1, 0))]
        valid_actions = [] # liste des actions valides
        agent, boxes = state # position de l'agent & des boxes

        # Add this node to explored nodes
        self.explored_nodes += 1

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

                if (new_box_x, new_box_y) not in self.walls and (new_box_x, new_box_y) not in boxes and not self.is_dead_state((new_box_x, new_box_y)):
                    valid_actions.append(action)
            else:
                valid_actions.append(action)
        return valid_actions

    def result(self, state, action):
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
    
    def is_dead_state(self, box):
        """Vérifie si la boite se retrouve dans des angles morts"""
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
        _, boxes = state
        return all(box in self.targets for box in boxes)
    
    def h(self, node):
        """Fonction heuristique pour les algorithmes de recherche informée"""
        if self.heuristic_type == 'greedy_matching':
            return greedy_matching_distance(self, node)
        else:
            return manhattan_distance(self, node)
    
    def path_cost(self, c, state1, action, state2):
        _, boxes1 = state1
        _, boxes2 = state2

        if boxes1 != boxes2:
            return c + 2
        return c + 1
    
    def get_explored_nodes(self):
        return self.explored_nodes
