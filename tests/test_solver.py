import unittest
import os
import sys
from pathlib import Path

# Add the parent directory to sys.path to import required modules
sys.path.append(str(Path(__file__).parent.parent))
from Sokoban import Sokoban
from game_board import getGameBoard
from aima.search import breadth_first_graph_search, depth_first_graph_search, astar_search

class TestSolver(unittest.TestCase):
    def setUp(self):
        # Use absolute paths to the level files
        self.test_dir = Path(__file__).parent.parent
        self.level = "01"
        self.init_file = os.path.join(self.test_dir, f"levels/sokoInst{self.level}.init")
        self.goal_file = os.path.join(self.test_dir, f"levels/sokoInst{self.level}.goal")
        
        # Set up the Sokoban problem
        agent, boxes, walls, width, height, targets = getGameBoard(self.init_file, self.goal_file)
        self.problem = Sokoban(initial=(agent, boxes), targets=targets, walls=walls)
        
    def test_bfs_solve(self):
        """Test solving with breadth-first search"""
        solution = breadth_first_graph_search(self.problem)
        
        # We should find a solution
        self.assertIsNotNone(solution)
        
        # The solution should be a valid path
        self.assertGreater(len(solution.path()), 1)
        
        # The final state should satisfy the goal test
        final_state = solution.state
        self.assertTrue(self.problem.goal_test(final_state))
        
    def test_dfs_solve(self):
        """Test solving with depth-first search"""
        solution = depth_first_graph_search(self.problem)
        
        # We should find a solution
        self.assertIsNotNone(solution)
        
        # The solution should be a valid path
        self.assertGreater(len(solution.path()), 1)
        
        # The final state should satisfy the goal test
        final_state = solution.state
        self.assertTrue(self.problem.goal_test(final_state))
    
    def test_astar_solve(self):
        """Test solving with A* search"""
        solution = astar_search(self.problem, h=self.problem.h)
        
        # We should find a solution
        self.assertIsNotNone(solution)
        
        # The solution should be a valid path
        self.assertGreater(len(solution.path()), 1)
        
        # The final state should satisfy the goal test
        final_state = solution.state
        self.assertTrue(self.problem.goal_test(final_state))
        
    def test_solution_path(self):
        """Test that the solution path is valid"""
        solution = breadth_first_graph_search(self.problem)
        path = solution.path()
        
        # Check that each step in the path is valid
        for i in range(1, len(path)):
            prev_state = path[i-1].state
            curr_state = path[i].state
            action = path[i].action
            
            # The current state should be reachable from the previous state via the action
            expected_state = self.problem.result(prev_state, action)
            self.assertEqual(curr_state, expected_state)

if __name__ == '__main__':
    unittest.main()