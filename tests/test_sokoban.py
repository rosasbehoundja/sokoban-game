import unittest
from Sokoban import Sokoban
from aima.search import breadth_first_graph_search

class TestSokoban(unittest.TestCase):
    def setUp(self):
        # Create a simple Sokoban problem for testing
        self.agent = (1, 1)
        self.boxes = frozenset([(2, 1)])
        self.walls = {(0, 0), (1, 0), (2, 0), (3, 0),
                      (0, 1),                 (3, 1),
                      (0, 2), (1, 2), (2, 2), (3, 2)}
        self.targets = {(2, 1)}  # Target at the same position as the box (already solved)
        
        self.initial_state = (self.agent, self.boxes)
        self.problem = Sokoban(initial=self.initial_state, targets=self.targets, walls=self.walls)
        
    def test_actions(self):
        """Test that the actions method returns valid actions"""
        actions = self.problem.actions(self.initial_state)
        
        # Should have at least left, up, and down (not right because there's a box)
        expected_actions = {'Left', 'Up', 'Down'}
        self.assertTrue(set(actions).issubset({'Up', 'Down', 'Left', 'Right'}))
        
        # Cannot move through walls
        self.assertNotIn('Right', actions)  # Box is to the right
        
    def test_result(self):
        """Test the result of an action"""
        # Move left
        new_state = self.problem.result(self.initial_state, 'Left')
        expected_agent = (0, 1)
        expected_boxes = self.boxes  # Boxes shouldn't change
        
        self.assertEqual(new_state, (expected_agent, expected_boxes))
        
        # Setup a state where we can push a box
        pushable_state = ((1, 1), frozenset([(2, 1)]))
        new_state = self.problem.result(pushable_state, 'Right')
        
        # Agent should move to (2, 1), box should move to (3, 1)
        expected_agent = (2, 1)
        expected_boxes = frozenset([(3, 1)])
        
        self.assertEqual(new_state[0], expected_agent)
        self.assertTrue((3, 1) in new_state[1])
        
    def test_goal_test(self):
        """Test the goal_test method"""
        # The initial state has the box on the target, so it should be a goal
        self.assertTrue(self.problem.goal_test(self.initial_state))
        
        # Create a state where the box is not on a target
        non_goal_state = ((1, 1), frozenset([(1, 1)]))
        problem = Sokoban(initial=non_goal_state, targets={(2, 1)}, walls=self.walls)
        
        self.assertFalse(problem.goal_test(non_goal_state))
        
    def test_dead_state(self):
        """Test the is_dead_state method for detecting boxes in corners"""
        # Test a corner position
        corner_pos = (1, 1)
        walls = {(0, 1), (1, 0)}  # Create a corner
        problem = Sokoban(initial=((0, 0), frozenset([(1, 1)])), targets={(2, 2)}, walls=walls)
        
        # Box at corner_pos with walls to the left and above is a dead state
        self.assertTrue(problem.is_dead_state(corner_pos))
        
        # A position that's not in a corner
        non_corner_pos = (2, 2)
        self.assertFalse(problem.is_dead_state(non_corner_pos))

if __name__ == '__main__':
    unittest.main()