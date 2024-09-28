# Artificial Intelligence 🤖🧠

**Solutions to practical assignments of Artificial Intelligence course (CE-417) at Sharif University of Technology**

This repository contains solutions for the practical assignments given in the AI course, covering various essential topics in artificial intelligence. Each assignment implements a specific AI technique or algorithm to solve real-world problems, showcasing the theoretical concepts in action.

## Topics of Assignments

* ###**HW1**:  
    * **A\***: Implements the A* search algorithm to solve an elevator scheduling problem where students and professors must be transported between two floors, following specific constraints.
    
      ![A* Algorithm GIF](a_star_algorithm.gif)
    
      **Problem Description**:
      The elevator needs to move students and professors between two floors with the following constraints:
      - No floor should have more students than professors (if professors are present).
      - The solution must ensure that all students and professors are transferred safely across floors.

      **Approach**:
      The problem is represented as a graph, where each state is described by the number of students and professors on each floor, and the position of the elevator. A* uses a heuristic to search for the optimal path from the initial to the final state, ensuring efficiency and optimality.
      
      **Comparison with DFS**:  
      The A* algorithm outperforms DFS in terms of finding shorter paths, thanks to its heuristic function, though it explores more states.

    * **Simulated Annealing**: Demonstrates optimization using the Simulated Annealing algorithm for solving the Knapsack problem.
    
      **Problem Description**:
      The Knapsack problem involves selecting a subset of items with specific weights and values to maximize the total value without exceeding a given weight limit.

      **Approach**:
      Simulated Annealing is a probabilistic algorithm that explores the solution space by accepting worse solutions with decreasing probability over time (as the temperature cools). This helps escape local optima and leads to a near-optimal solution.

      **Results**:  
      The algorithm finds an average best solution with a value of approximately 2595.05 over multiple runs, demonstrating its effectiveness in solving the Knapsack problem.

* **HW2**:  
    * **Cryptarithmetic Puzzle**: Solving word puzzles as constraint satisfaction problems.
    * **Adversarial Search**: Minimax algorithm for game-playing agents with alpha-beta pruning.
    
* **HW3**:  
    * **Q-Tabular**: Implementation of Q-learning with tabular updates for reinforcement learning.
    * **RL Chat**: A simple chat system utilizing reinforcement learning for decision-making.
    
* **HW4**:  
    * **Bayesian Networks**: Building and inference on Bayesian networks for probabilistic reasoning.
    
* **HW5**:  
    * **Decision Tree**: Implementing decision tree algorithms for classification tasks.
    * **Logistic Regression**: Logistic regression for binary classification.

## Installation & Usage 💻

### Prerequisites
- Python 3.x

## Instructor ✍
[Professor Mohammad Hossein Rohban](https://www.linkedin.com/in/mohammad-hossein-rohban-75567677/?originalSubdomain=ir)

## Contribution 👥
Feel free to fork this repository, submit pull requests, or raise issues if you find any bugs or have suggestions for improvements.
