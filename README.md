# Sokoban Project

This project is developed as part of the Research Techniques course.

## Description

Sokoban is a puzzle game where the player must push boxes onto target locations in a maze. The goal is to solve each level by placing all the boxes on the targets while adhering to the following rules:
- Boxes can only be pushed one at a time.
- The player cannot pull boxes, only push them.
- The player cannot pass through walls or boxes.

![Representation](media/image.png)

- @ represents the agent
- "#" represents the walls
- $ represents the boxes
- . reprensents the boxes targets position

## Project Objectives

- Implement a functional version of the Sokoban game.
- Explore and apply search techniques to automatically solve game levels.
- Study and compare different algorithmic approaches to solving the puzzles.

## Project Structure

- **Source Code**: Contains the implementation of the game and solving algorithms.
- **Documentation**: Provides explanations of the algorithms used and design choices.
- **Tests**: Includes test levels and scripts to validate solutions.

## Prerequisites

- Python 3.x
- Required libraries (to be installed via `requirements.txt`)

## Installation

1. Clone the project repository:
    ```bash
    git clone https://github.com/rosasbehoundja/sokoban-game.git
    cd sokoban-game
    ```
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. To execute the automatic solving algorithms:
    ```bash
    python solve.py <game_level> <algorithm_choice>
    ```

![Demo video](media/output.gif)

## Authors

This project was created by IFRI students as part of the Research Techniques course.

 - [Emmanuella GBODO](gbodoemmanuella40@gmail.com)
 - [Rosas BEHOUNDJA](perrierosas@gmail.com)