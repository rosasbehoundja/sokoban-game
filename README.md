# Sokoban Project

This project was developed as part of the Search Techniques course.

## Description

Sokoban is a puzzle game where the player must push boxes onto target locations in a maze. The objective is to solve each level by placing all the boxes on the targets while following these rules:
- Boxes can only be pushed one at a time.
- The player cannot pull boxes, only push them.
- The player cannot move through walls or boxes.

```
        ##########                ##########
        #        #                #    .   #
        #   $  $ #                #        #
        #@       #                #     .  #
        ##########                ##########

        Initial State             Goal Positions
```

- @ represents the agent
- "#" represents walls
- $ represents boxes
- . represents target positions for the boxes

## Project Objectives

- Implement a functional version of the Sokoban game.
- Explore and apply search techniques to automatically solve game levels.
- Study and compare different algorithmic approaches to solve the puzzles.

## Project Structure

- **Source Code**: Contains the game implementation and solution algorithms.
- **Documentation**: Provides explanations of the algorithms used and design choices.
- **Tests**: Includes test levels and scripts to validate solutions.

## Implemented Heuristics

The project offers several admissible heuristics to guide informed search algorithms (A* and GBFS):

### 1. Manhattan Distance (manhattan)
- **Description**: Calculates the sum of Manhattan distances between each box and its closest target.
- **Complexity**: O(n×m) where n is the number of boxes and m the number of targets.
- **Advantages**: Simple and quick to calculate.
- **Disadvantages**: May overestimate the actual difficulty as multiple boxes can be assigned to the same target.

### 2. Greedy Matching Distance (greedy_matching)
- **Description**: An intermediate heuristic that greedily assigns each box to its closest target, ensuring that each target is assigned to only one box.
- **Complexity**: O(n²) where n is the number of boxes/targets.
- **Advantages**: Good balance between accuracy and calculation speed. Avoids the multiple assignment problem of Manhattan distance.
- **Recommended Use**: For medium to high difficulty levels.

## Recommendations for Using Heuristics
- **Simple levels**: Manhattan Distance (manhattan) - fastest
- **Complex levels**: Greedy Matching (greedy_matching) - good balance

## Prerequisites

- Python 3.x
- Required libraries (install via `requirements.txt`)

## Installation

1. Clone the project repository:
    ```bash
    git clone https://github.com/rosasbehoundja/sokoban-game.git
    cd sokoban-game
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. To run the automatic solution algorithms:
    ```bash
    python solve.py -l <game_level> -m <algorithm_choice> -hu <heuristic>
    ```
    
    Examples:
    ```bash
    # Use A* with greedy matching heuristic
    python solve.py -l 01 -m astar -hu greedy_matching
    
    # Use Greedy Best-First Search with manhattan distance
    python solve.py -l 02 -m gbfs -hu manhattan
    ```

## Authors

This project was created by IFRI students as part of the Search Techniques course.

 - [Emmanuella GBODO](mailto:gbodoemmanuella40@gmail.com)
 - [Rosas BEHOUNDJA](rosasbehoundja.github.io)