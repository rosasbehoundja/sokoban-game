"""
Input & Output Format - Sokoban Game

Authors: Emmanuella GBODO (gbodoemmanuella40@gmail.com)
         Rosas BEHOUNDJA (perrierosas@gmail.com)
"""
import numpy as np

def getGameBoard(initial_positions, target_positions) -> np.ndarray:
    """
    Args:
        initial_positions (sokoInstXX.init): Initial positions of the boxes and the agent.
        target_positions (sokoInstXX.goal): Target positions of the boxes.

    Returns:
        board (np.ndarray): Game configuration with agent position, walls, boxes, and goals positions.
    """
