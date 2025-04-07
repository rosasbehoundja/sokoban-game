import unittest
import subprocess
import sys
import os
from pathlib import Path

# For importing from parent directory
sys.path.append(str(Path(__file__).parent.parent))

class TestSystem(unittest.TestCase):
    def setUp(self):
        # Set the working directory to the parent directory for running the solve.py script
        self.project_dir = Path(__file__).parent.parent
        os.chdir(self.project_dir)
    
    def test_solve_level01_bfs(self):
        """System test for solving level 01 with BFS"""
        # Run the solve.py script with level 01 and BFS method
        result = subprocess.run([sys.executable, "solve.py", "--level", "01", "--method", "bfs"], 
                               capture_output=True, text=True)
        
        # Check the exit code
        self.assertEqual(result.returncode, 0)
        
        # Check output contains expected text
        self.assertIn("Solution trouvée", result.stdout)
        
    def test_solve_level01_dfs(self):
        """System test for solving level 01 with DFS"""
        # Run the solve.py script with level 01 and DFS method
        result = subprocess.run([sys.executable, "solve.py", "--level", "01", "--method", "dfs"], 
                               capture_output=True, text=True)
        
        # Check the exit code
        self.assertEqual(result.returncode, 0)
        
        # Check output contains expected text
        self.assertIn("Solution trouvée", result.stdout)
        
    def test_solve_level01_astar(self):
        """System test for solving level 01 with A*"""
        # Run the solve.py script with level 01 and A* method
        result = subprocess.run([sys.executable, "solve.py", "--level", "01", "--method", "astar"], 
                               capture_output=True, text=True)
        
        # Check the exit code
        self.assertEqual(result.returncode, 0)
        
        # Check output contains expected text
        self.assertIn("Solution trouvée", result.stdout)
        
    def test_solve_level01_gbfs(self):
        """System test for solving level 01 with GBFS"""
        # Run the solve.py script with level 01 and GBFS method
        result = subprocess.run([sys.executable, "solve.py", "--level", "01", "--method", "gbfs"], 
                               capture_output=True, text=True)
        
        # Check the exit code
        self.assertEqual(result.returncode, 0)
        
        # Check output contains expected text
        self.assertIn("Solution trouvée", result.stdout)
        
    def test_invalid_method(self):
        """Test with an invalid method argument"""
        # Run with invalid method
        result = subprocess.run([sys.executable, "solve.py", "--level", "01", "--method", "invalid"], 
                               capture_output=True, text=True)
        
        # Should still exit with code 0 but indicate method is invalid
        self.assertEqual(result.returncode, 0)
        self.assertIn("Méthode invalide", result.stdout)
        
    def test_levels_existence(self):
        """Test that all required level files exist"""
        # Check for first 10 levels
        for i in range(1, 11):
            level = f"{i:02d}"
            init_file = os.path.join(self.project_dir, f"levels/sokoInst{level}.init")
            goal_file = os.path.join(self.project_dir, f"levels/sokoInst{level}.goal")
            
            self.assertTrue(os.path.exists(init_file), f"Missing file: {init_file}")
            self.assertTrue(os.path.exists(goal_file), f"Missing file: {goal_file}")

if __name__ == '__main__':
    unittest.main()