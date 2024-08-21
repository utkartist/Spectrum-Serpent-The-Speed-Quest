import pygame
import time
import random
import os

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
gold = (255, 215, 0)
purple = (160, 32, 240)
grey = (169, 169, 169)
meteor_color = (105, 105, 105)  # Dark Grey for meteors
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

# Set the dimensions of the display
dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
initial_speed = 5
speed_increment = 0.5  # Slower speed increase to make the game more manageable
max_speed = 20  # Lower max speed for better playability

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def generate_special_fruit():
    special_fruit_type = random.choice(['golden', 'poisoned'])
    special_fruit_position = [round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0,
                              round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0]
    return special_fruit_type, special_fruit_position

def draw_special_fruit(special_fruit_type, special_fruit_position):
    if special_fruit_type == 'golden':
        color = gold
    elif special_fruit_type == 'poisoned':
        color = purple
    pygame.draw.rect(dis, color, [special_fruit_position[0], special_fruit_position[1], snake_block, snake_block])

def generate_power_up():
    power_up_type = random.choice(['speed', 'slow', 'invincibility'])
    power_up_position = [round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0,
                         round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0]
    return power_up_type, power_up_position

def draw_power_up(power_up_type, power_up_position):
    if power_up_type == 'speed':
        color = yellow
    elif power_up_type == 'slow':
        color = blue
    elif power_up_type == 'invincibility':
        color = red
    pygame.draw.rect(dis, color, [power_up_position[0], power_up_position[1], snake_block, snake_block])

def generate_obstacles(num_obstacles):
    obstacles = []
    for _ in range(num_obstacles):
        obstacle_position = [round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0,
                             round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0]
        obstacles.append(obstacle_position)
    return obstacles

def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(dis, black, [obstacle[0], obstacle[1], snake_block, snake_block])

def our_snake(snake_block, snake_list):
    for index, x in enumerate(snake_list):
        color = colors[index % len(colors)]
        pygame.draw.rect(dis, color, [x[0], x[1], snake_block, snake_block])

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Meteor Functions
def generate_meteor():
    meteor_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    meteor_y = 0  # Start at the top of the screen
    meteor_speed = random.randint(5, 10)  # Slower meteors for more manageable gameplay
    return [meteor_x, meteor_y, meteor_speed]

def draw_meteor(meteor):
    pygame.draw.rect(dis, meteor_color, [meteor[0], meteor[1], snake_block, snake_block])

def move_meteors(meteors):
    for meteor in meteors:
        meteor[1] += meteor[2]  # Move the meteor down the screen

def check_meteor_collision(meteors, snake_head):
    for meteor in meteors:
        if meteor[0] == snake_head[0] and meteor[1] == snake_head[1]:
            return True
    return False

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    snake_speed = initial_speed
    obstacles = generate_obstacles(5)  # Start with 5 obstacles
    power_up_active = False
    special_fruit_active = False

    # Timers for when to spawn the next power-up and special fruit
    next_power_up_time = pygame.time.get_ticks() + random.randint(5, 10) * 1000
    next_special_fruit_time = pygame.time.get_ticks() + random.randint(7, 12) * 1000

    # Meteor Shower Variables
    meteors = []
    next_meteor_time = pygame.time.get_ticks() + random.randint(5, 10) * 1000  # Meteors every 5-10 seconds
    max_meteors = 3  # Limit the number of meteors on screen

    score = 0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        draw_obstacles(obstacles)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # Power-Up Logic
        if pygame.time.get_ticks() > next_power_up_time:
            power_up_type, power_up_position = generate_power_up()
            power_up_active = True
            next_power_up_time = pygame.time.get_ticks() + random.randint(5, 10) * 1000
        if power_up_active:
            draw_power_up(power_up_type, power_up_position)

        # Special Fruit Logic
        if pygame.time.get_ticks() > next_special_fruit_time:
            special_fruit_type, special_fruit_position = generate_special_fruit()
            special_fruit_active = True
            next_special_fruit_time = pygame.time.get_ticks() + random.randint(7, 12) * 1000
        if special_fruit_active:
            draw_special_fruit(special_fruit_type, special_fruit_position)

        # Meteor Shower Logic
        if pygame.time.get_ticks() > next_meteor_time and len(meteors) < max_meteors:
            meteors.append(generate_meteor())
            next_meteor_time = pygame.time.get_ticks() + random.randint(5, 10) * 1000
        
        move_meteors(meteors)
        for meteor in meteors:
            draw_meteor(meteor)

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        if check_meteor_collision(meteors, snake_Head):
            game_close = True

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for obstacle in obstacles:
            if x1 == obstacle[0] and y1 == obstacle[1]:
                game_close = True

        if power_up_active and x1 == power_up_position[0] and y1 == power_up_position[1]:
            if power_up_type == 'speed':
                snake_speed += 5
            elif power_up_type == 'slow':
                snake_speed -= 2
            elif power_up_type == 'invincibility':
                # Implement invincibility logic
                pass
            power_up_active = False  # Remove the power-up after it is collected

        if special_fruit_active and x1 == special_fruit_position[0] and y1 == special_fruit_position[1]:
            if special_fruit_type == 'golden':
                score += 10  # Extra points for Golden Fruit
            elif special_fruit_type == 'poisoned':
                Length_of_snake -= 1  # Reduce snake length by 1, but not less than 1
                if Length_of_snake < 1:
                    Length_of_snake = 1
            special_fruit_active = False  # Remove the special fruit after it is collected

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 1
            if snake_speed < max_speed:
                snake_speed += speed_increment

            if score % 5 == 0 and len(obstacles) < 15:  # Add more obstacles as score increases
                new_obstacle = generate_obstacles(1)
                obstacles.extend(new_obstacle)

        # Remove meteors that have fallen off the screen
        meteors = [meteor for meteor in meteors if meteor[1] < dis_height]

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
