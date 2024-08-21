# Snake Game with Power-Ups and Meteor Shower

## Overview
This is a modernized version of the classic Snake game built using Python and the Pygame library. The game introduces several new features to enhance the gameplay experience, including special fruits, power-ups, obstacles, and a challenging meteor shower. Players must navigate the snake to collect food while avoiding obstacles, meteors, and the snake's own body.

## Features

### 1. Classic Snake Gameplay
The snake grows longer each time it consumes food. The player's objective is to control the snake, avoiding collisions with the screen boundaries, obstacles, and the snake's body.

### 2. Special Fruits
- **Golden Fruit**: Grants 10 bonus points when collected.
- **Poisoned Fruit**: Reduces the snake's length by 1 segment, but the length will not go below 1 segment.

Special fruits appear at random intervals and locations, adding an extra layer of strategy to the game.

### 3. Power-Ups
- **Speed Boost**: Temporarily increases the snake's speed, making it harder to control but rewarding skilled players.
- **Slow Down**: Temporarily decreases the snake's speed, making it easier to navigate tight spaces.
- **Invincibility**: Grants temporary immunity to collisions with obstacles and meteors, allowing players to collect food more easily.

Power-ups appear at random intervals and can significantly impact gameplay, offering players tactical advantages.

### 4. Obstacles
Static obstacles are randomly placed on the screen. The snake must avoid these obstacles to survive. As the game progresses, more obstacles are added to increase the difficulty.

### 5. Meteor Shower
Meteors fall from the top of the screen at random intervals. Players must avoid these meteors to prevent the game from ending. The meteors add an unpredictable element to the game, requiring quick reflexes and strategic movement.

The number of meteors on the screen is limited to prevent the game from becoming overwhelming.

### 6. Dynamic Difficulty
The game's difficulty increases as the player's score rises. The snake's speed gradually increases, and more obstacles are added to the screen. The player must adapt to the increasing challenge to achieve a high score.

## Installation

To play the game, you need to have Python and Pygame installed on your system.

### Steps to Install:

1. **Install Python**: Download and install Python from the [official website](https://www.python.org/).
2. **Install Pygame**: Open a terminal or command prompt and run the following command:

    ```bash
    pip install pygame
    ```

3. **Clone the Repository**: Download or clone this repository to your local machine.

    ```bash
    git clone https://github.com/utkartist/snake-game.git
    ```

4. **Navigate to the Project Directory**:

    ```bash
    cd snake-game
    ```

## How to Play

1. **Run the Game**: Open a terminal or command prompt, navigate to the directory containing the game files, and run the following command:

    ```bash
    python snake_game.py
    ```

2. **Gameplay Controls**:
   - Use the arrow keys to control the direction of the snake.
   - Collect food to grow longer and increase your score.
   - Avoid colliding with obstacles, meteors, the screen edges, and your own tail.
   - Collect special fruits and power-ups for bonuses and temporary effects.

3. **Game Over**:
   - The game ends when the snake collides with an obstacle, meteor, the screen edges, or its own body. Press `C` to play again or `Q` to quit.

## Code Structure

- **`snake_game.py`**: The main game file containing all the logic for gameplay, including snake movement, collision detection, meteor shower, and power-ups.

### Key Functions:

- **`generate_special_fruit()`**: Randomly generates a special fruit on the screen with either beneficial or harmful effects.
- **`draw_special_fruit()`**: Draws the special fruit on the screen.
- **`generate_power_up()`**: Randomly generates a power-up with various gameplay effects.
- **`draw_power_up()`**: Draws the power-up on the screen.
- **`generate_obstacles()`**: Creates a list of static obstacles on the screen.
- **`draw_obstacles()`**: Renders the obstacles on the screen.
- **`generate_meteor()`**: Generates meteors at random positions at the top of the screen that fall downward.
- **`draw_meteor()`**: Draws meteors on the screen.
- **`move_meteors()`**: Updates the position of meteors, making them fall from the top to the bottom of the screen.
- **`check_meteor_collision()`**: Checks if the snake's head has collided with any meteors.

## Customization

Feel free to modify the game's parameters, such as the speed of the snake, the frequency of power-ups, and the number of obstacles. The code is well-commented, making it easy to understand and customize according to your preferences.

