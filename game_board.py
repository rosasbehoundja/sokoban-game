

def getGameBoard(initial_positions, target_positions):
    """
    Args:
        initial_positions (sokoInstXX.init): Initial positions of the boxes and the agent.
        target_positions (sokoInstXX.goal): Target positions of the boxes.

    Returns:

    """
    agent, boxes, walls, width, height = parse_init_file(initial_positions)
    target = parse_goal_file(target_positions)

    return agent, boxes, walls, width, height, target

def print_state(state, walls, width, height, targets):
    """Permet d'afficher les états"""
    agent, boxes = state
    grid = []
    for y in range(height):
        row = []
        for x in range(width):
            if (x, y) in walls:
                row.append('#')
            elif (x, y) == agent:
                row.append('@')
            elif (x, y) in boxes:
                row.append('$')
            elif (x, y) in targets:
                row.append('.')
            else:
                row.append(' ')
        grid.append(''.join(row))
    print('\n'.join(grid))


def parse_init_file(filename):
    walls = set()
    boxes = set()
    agent = None
    with open(filename, 'r') as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line.strip()):
                if char == '#':
                    walls.add((x, y))
                elif char == '@':
                    agent = (x, y)
                elif char == '$':
                    boxes.add((x, y))

        width, height = x + 1, y + 1 # récupérer les dimensions de la grille

    return agent, frozenset(boxes), walls, width, height

def parse_goal_file(filename):
    target = set()
    with open(filename, "r") as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line.strip()):
                if char == ".":
                    target.add((x, y))
    return target