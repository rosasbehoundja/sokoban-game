import unittest
import os
import sys
from pathlib import Path

# Add the parent directory to sys.path to import game_board
sys.path.append(str(Path(__file__).parent.parent))
from game_board import getGameBoard, parse_init_file, parse_goal_file

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        # Use absolute paths to the level files
        self.test_dir = Path(__file__).parent.parent
        self.test_init_file = os.path.join(self.test_dir, "levels/sokoInst01.init")
        self.test_goal_file = os.path.join(self.test_dir, "levels/sokoInst01.goal")
        
    def test_parse_init_file(self):
        """Test the parsing of initialization files"""
        agent, boxes, walls, width, height = parse_init_file(self.test_init_file)
        
        # Check agent position
        self.assertIsNotNone(agent)
        self.assertIsInstance(agent, tuple)
        self.assertEqual(len(agent), 2)
        
        # Check boxes
        self.assertIsNotNone(boxes)
        self.assertTrue(hasattr(boxes, '__iter__'))  # Should be iterable (set)
        
        # Check walls
        self.assertIsNotNone(walls)
        self.assertTrue(hasattr(walls, '__iter__'))  # Should be iterable (set)
        
        # Check dimensions
        self.assertGreater(width, 0)
        self.assertGreater(height, 0)
        
    def test_parse_goal_file(self):
        """Test the parsing of goal files"""
        targets = parse_goal_file(self.test_goal_file)
        
        # Check targets
        self.assertIsNotNone(targets)
        self.assertTrue(hasattr(targets, '__iter__'))  # Should be iterable (set)
        self.assertGreater(len(targets), 0)  # Should have at least one target
        
    def test_getGameBoard(self):
        """Test the main getGameBoard function"""
        agent, boxes, walls, width, height, targets = getGameBoard(self.test_init_file, self.test_goal_file)
        
        # Basic validation of returned values
        self.assertIsNotNone(agent)
        self.assertIsNotNone(boxes)
        self.assertIsNotNone(walls)
        self.assertIsNotNone(targets)
        self.assertGreater(width, 0)
        self.assertGreater(height, 0)
        
        # Check matching number of boxes and targets
        self.assertEqual(len(boxes), len(targets))

if __name__ == '__main__':
    unittest.main()