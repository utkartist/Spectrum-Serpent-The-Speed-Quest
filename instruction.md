# Snake Game with Power-Ups and Meteor Shower

## Overview

This is a modern twist on the classic Snake game, built using Python and the Pygame library. Navigate the snake to collect food and grow longer, while avoiding obstacles, meteors, and the snake's own body. Special fruits and power-ups add an exciting layer to the game, offering both advantages and challenges.

## Color Guide

### Snake
- **Multi-colored**: The snake is made up of blocks that change color. The colors alternate to make the snake visually appealing as it grows longer.

### Food
- **Green**: Represents the standard food. Eating this makes the snake grow longer and increases your score.

### Special Fruits
- **Gold**: Represents the Golden Fruit. Collecting this gives you 10 bonus points.
- **Purple**: Represents the Poisoned Fruit. Collecting this reduces the snake’s length by 1, but it won't shrink below a single block.

### Power-Ups
- **Yellow**: Speed Boost – Temporarily increases the snake’s speed, making it more challenging to control.
- **Blue**: Slow Down – Temporarily decreases the snake’s speed, making it easier to navigate.
- **Red**: Invincibility – Temporarily makes the snake immune to collisions with obstacles and meteors.

### Obstacles
- **Black**: Static obstacles that appear randomly on the screen. Avoid these to keep playing.

### Meteors
- **Dark Grey**: Falling meteors that appear at random intervals. Avoid these as they can end the game instantly if they hit the snake.

## How to Play

### Controls
- **Arrow Keys**: Use the arrow keys to move the snake up, down, left, or right.

### Objective
- **Grow the Snake**: Eat the green food blocks to make the snake grow longer.
- **Avoid Collisions**: Don’t crash into the walls, obstacles, meteors, or your own snake’s body.

### Special Fruits and Power-Ups
- **Special Fruits**: Occasionally, special fruits (gold or purple) will appear on the screen. Collect them for bonus points or to reduce your length strategically.
- **Power-Ups**: Collect power-ups (yellow, blue, or red) for temporary effects that can either help or challenge you.

### Meteors
- **Meteors**: Meteors will fall from the top of the screen. Dodge them to keep playing. There will be a maximum of three meteors on the screen at any time, so stay alert!

### Game Over
- The game ends when the snake collides with an obstacle, meteor, the screen edges, or its own body.
- **Restart**: Press `C` to play again.
- **Quit**: Press `Q` to quit the game.

## Installation

### Requirements
- **Python**: Make sure Python is installed on your system. You can download it from the [official website](https://www.python.org/).
- **Pygame**: Install the Pygame library by running the following command:
    ```bash
    pip install pygame
    ```

### Running the Game
1. **Download the Game**: Clone or download the repository to your local machine.
    ```bash
    git clone https://github.com/yourusername/snake-game.git
    ```
2. **Navigate to the Game Directory**:
    ```bash
    cd snake-game
    ```
3. **Run the Game**:
    ```bash
    python snake_game.py
    ```

## Customization

Feel free to modify the game’s parameters, such as snake speed, power-up frequency, and obstacle count. The code is well-commented to help you understand and tweak the gameplay to your liking.
