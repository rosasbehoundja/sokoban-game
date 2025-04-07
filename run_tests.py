import unittest
import sys
import os
from pathlib import Path

# Ensure the test directory is in the path
test_dir = os.path.join(Path(__file__).parent, 'tests')
sys.path.append(test_dir)

# Import test classes
from tests.test_gameboard import TestGameBoard
from tests.test_sokoban import TestSokoban
from tests.test_solver import TestSolver
from tests.test_system import TestSystem

def create_test_suite():
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_suite.addTest(unittest.makeSuite(TestGameBoard))
    test_suite.addTest(unittest.makeSuite(TestSokoban))
    test_suite.addTest(unittest.makeSuite(TestSolver))
    test_suite.addTest(unittest.makeSuite(TestSystem))
    
    return test_suite

if __name__ == '__main__':
    # Set the working directory to the project root
    os.chdir(Path(__file__).parent)
    
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = create_test_suite()
    runner.run(test_suite)