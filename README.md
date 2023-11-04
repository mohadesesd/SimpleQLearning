# Simple Q-Learning Model for Grid Game

## Introduction

This repository contains a Python implementation of a basic Q-learning algorithm applied to a simple grid-based game. The game environment is a 4x5 grid where an agent learns to navigate from a starting point to a destination.

## Game Environment

- **Grid Size**: 4 rows x 5 columns
- **Actions**: 4 (up, down, right, left)
- **Rewards**: The agent receives different rewards as it navigates through the grid, with a goal to maximize its total reward.

## Q-Learning Model

The Q-learning model is a form of reinforcement learning that does not require a model of the environment and can handle problems with stochastic transitions and rewards, without requiring adaptations.

For this specific application:
- **Learning Rate (`lr`)**: 0.2
- **Discount Factor (`gamma`)**: 0.8
- **Exploration Rate (`epsilon`)**: 0.1

The agent learns by exploring the environment and exploiting the learned values in the Q-table.

## Requirements

To run this script, you need:
- Python 3.x
- NumPy library
