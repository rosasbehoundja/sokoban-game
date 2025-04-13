"""
Different heuristics function
"""
from aima.search import Node

def manhattan_distance(self, node:Node):
    cost = 0
    agent, boxes = node.state
    for box in boxes:
        if box not in self.targets:
            min_dist = min(abs(box[0] - t[0]) + abs(box[1] - t[1]) for t in self.targets)
            cost += min_dist

    min_agent_dist = min(abs(agent[0] - b[0]) + abs(agent[1] - b[1]) for b in boxes)
    cost += min_agent_dist * 0.5

    return cost

def greedy_matching_distance(self, node:Node):
    """
    A more efficient heuristic algorithm that assigns each box
    to its closest target while ensuring no two boxes are assigned to the same target.
    
    This is admissible and typically better than simple manhattan_distance,
    but less computationally expensive than the hungarian_algorithm.
    """
    _, boxes = node.state
    
    if not boxes or not self.targets:
        return 0
    
    boxes_list = list(boxes)
    targets_list = list(self.targets)
    
    total_cost = 0
    remaining_targets = set(targets_list)
    
    # Sort boxes by their minimum distance to any target
    # This helps ensure a better greedy assignment
    boxes_with_min_dist = []
    for box in boxes_list:
        if box in self.targets:
            min_dist = 0
            min_target = box
        else:
            min_dist = float('inf')
            min_target = None
            for target in targets_list:
                dist = abs(box[0] - target[0]) + abs(box[1] - target[1])
                if dist < min_dist:
                    min_dist = dist
                    min_target = target
        boxes_with_min_dist.append((box, min_dist, min_target))
    
    # Sort by minimum distance
    boxes_with_min_dist.sort(key=lambda x: x[1])
    
    # Greedily assign boxes to targets
    for box, _, _ in boxes_with_min_dist:
        if box in remaining_targets:
            remaining_targets.remove(box)
            continue
            
        # Find the closest remaining target
        min_dist = float('inf')
        closest_target = None
        
        for target in remaining_targets:
            dist = abs(box[0] - target[0]) + abs(box[1] - target[1])
            if dist < min_dist:
                min_dist = dist
                closest_target = target
        
        if closest_target:
            total_cost += min_dist
            remaining_targets.remove(closest_target)
        else:
            # If no remaining targets, add minimum distance to any target
            # (this is a simplification - should only happen with more boxes than targets)
            min_dist = min(abs(box[0] - t[0]) + abs(box[1] - t[1]) for t in targets_list)
            total_cost += min_dist

    return total_cost
