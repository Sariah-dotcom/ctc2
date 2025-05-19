import pygame
import math
import random

pygame.init()
pygame.mixer.init()

scores = []

# Create game window
SCREEN_HEIGHT, SCREEN_WIDTH = 700, 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Catch the Commandments')
clock = pygame.time.Clock()

# Background Music
pygame.mixer.music.load('music/bg-music.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

background = pygame.image.load('images/background.png')
prompt = pygame.image.load('images/prompt.png')
prompt2 = pygame.image.load('images/prompt-2.png')

def render_background():
    screen.blit(background, (0, 0))

def render_prompt():
    screen.blit(prompt, (SCREEN_WIDTH // 2 - prompt.get_width() // 2, 590))

def render_prompt2():
    screen.blit(prompt2, (SCREEN_WIDTH // 2 - prompt.get_width() // 2 - 80, 590))

def render_score():
    # Display score
    scoreCard = pygame.image.load('images/final-score-card.png')
    screen.blit(scoreCard, (SCREEN_WIDTH // 2 - scoreCard.get_width() // 2, 220))

    font_path = 'fonts/ConcertOne-Regular.ttf'
    font = pygame.font.Font(font_path, 35)
    score_text = font.render(f"Final Score: {current_score}", True, black)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 320))

    scores.append(current_score)

    if scores:
        highest_score = max(scores)
        highest_score_text = font.render(f"High Score: {highest_score}", True, black)
        screen.blit(highest_score_text, (SCREEN_WIDTH // 2 - highest_score_text.get_width() // 2, 380))

running = True
black = (0,0,0)

# Title screen
def title_screen():
    global running
    angle = 0 

    while running:
        render_background()

        title = pygame.image.load('images/title.png')
        title_x = SCREEN_WIDTH // 2 - title.get_width() // 2
        title_y = 50
        base_y = title_y

        '''Title animation'''
        speed = 2.5  # Speed of the animation
        amplitude = 20  # Max distance up and down

        angle += speed  # Increment the angle
        title_y = base_y + amplitude * math.sin(math.radians(angle))

        if angle >= 360:
            angle -= 360

        # Draw title image
        screen.blit(title, (title_x, title_y))
        clock.tick(60)

        palms = pygame.image.load('images/hands-with-glow.png')
        screen.blit(palms, (SCREEN_WIDTH // 2 - palms.get_width() // 2, SCREEN_HEIGHT // 2 - palms.get_height() // 2 +80))
        render_prompt()
        
        pygame.display.update()

        #Wait for key press
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                return
#Quiz
questions = [
    {
        "question": "What law was given to the Saints in D&C 42?",
        "options": ["Law of Concentration", "Law of Communion", "Law of Baptism", "Law of Consecration"],
        "answer": "Law of Consecration"
    },
    {
        "question": "What did Joseph Smith read that lead to the First Vision?",
        "options": ["James 1:5", "John 2:25", "1 Nephi 3:7", "Hebrews 1:11"],
        "answer": "James 1:5"
    },{
        "question": "Which book is not apart of the LDS Standard works?",
        "options": ["The Old Testament", "D&C", "The Book of Jubilees", "Pearl of Great Price"],
        "answer": "The Book of Jubilees"
    },
    {
        "question": "Look unto me in every _____; doubt not, _____ not?",
        "options": ["thought, fear", "thing, dispute ", "prayer, kill", "action, stop"],
        "answer": "thought, fear"
    },{
        "question": "'Disciple' comes from the word...",
        "options": ["Discipleship", "Principles", "Discipline", "Discernment"],
        "answer": "Discipline"
    },{
        "question": "I will go and do the things the Lord commands' is found in?",
        "options": ["D&C 36:6", "John 3:17", "1 Nephi 3:7", "Isaiah 30:2"],
        "answer": "1 Nephi 3:7"
    },{
        "question": "We become disciples of Jesus Christ when we...",
        "options": ["Hear and do His Word", "Read His Word", "Hear His Word", "Pray"],
        "answer": "Hear and do His Word"
    },{
        "question": "Jesus Christ is our ______ with the Father",
        "options": ["Lord", "Saviour", "Advocate", "Friend"],
        "answer": "Advocate"
    },{
        "question": "To consecrate means to...",
        "options": ["Pray fervently", "Give to the poor", "To follow the covenant path", "Set aside something for a sacred purpose"],
        "answer": "Set aside something for a sacred purpose"
    }
]

current_question = 0
question_score = 0

def quiz():
    global count

    # Pick a random question
    question = random.choice(questions)
    selected_option = None
    font = pygame.font.Font(font_path, 32)
    small_font = pygame.font.Font(font_path, 26)

    # Set a 15-second timer (in milliseconds)
    start_time = pygame.time.get_ticks()
    time_limit = 12000  # 10 seconds

    while True:
        render_background()

        # Draw question box
        text_box = pygame.image.load('images/card.png')
        screen.blit(text_box, (SCREEN_WIDTH // 2 - text_box.get_width() // 2, 100))

        # Render question
        intro_text = font.render("Oh no, you caught some bad stuff!", True, (200, 0, 0))
        question_text = font.render(question["question"], True, black)
        screen.blit(intro_text, (SCREEN_WIDTH // 2 - intro_text.get_width() // 2, 140))
        screen.blit(question_text, (SCREEN_WIDTH // 2 - question_text.get_width() // 2, 210))

        # Render options (A–D)
        for i, option in enumerate(question["options"]):
            label = chr(65 + i)  # 'A', 'B', ...
            option_text = small_font.render(f"{label}) {option}", True, black)
            screen.blit(option_text, (SCREEN_WIDTH // 2 - 200, 250 + i * 50))

        # Display remaining time
        elapsed_time = pygame.time.get_ticks() - start_time
        remaining_time = max(0, (time_limit - elapsed_time) // 1000)
        timer_text = small_font.render(f"Time left: {remaining_time}s", True, (200, 0, 0))
        screen.blit(timer_text, (SCREEN_WIDTH // 2 + 150, 500))

        pygame.display.update()

        # Check for timeout
        if elapsed_time >= time_limit:
            render_background()
            game_over()
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if pygame.K_a <= event.key <= pygame.K_d:
                    selected_index = event.key - pygame.K_a
                    selected_option = question["options"][selected_index]

                    if selected_option == question["answer"]:
                        count = 0  # Reset count
                        return  # Resume game
                    else:
                        render_background()
                        game_over()
                        return

# Instructions
def instructions():
    global running
    while True:
        render_background()

        instuction_title = pygame.image.load('images/instruction-title.png')
        screen.blit(instuction_title, (SCREEN_WIDTH //2 - instuction_title.get_width()//2, 10))
        
        text_box = pygame.image.load('images/instructions.png')
        screen.blit(text_box, (SCREEN_WIDTH //2 - text_box.get_width()//2, 100))

        pygame.display.update()

        #Wait for key press
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                return

#Ingredient images
def load_and_scale(path, scale=0.35):
    img = pygame.image.load(path)
    width, height = img.get_size()
    return pygame.transform.smoothscale(img, (int(width * scale), int(height * scale)))

def load_and_scale2(path, scale=0.5):
    img = pygame.image.load(path)
    width, height = img.get_size()
    return pygame.transform.smoothscale(img, (int(width * scale), int(height * scale)))

ingredientImgs = [
    load_and_scale('images/good/pray.png'),
    load_and_scale('images/good/heart.png'),
    load_and_scale('images/good/bread.png'),
    load_and_scale2('images/good/Bible.png'),
    load_and_scale('images/good/water.png'),
    load_and_scale('images/good/church.png'),
    load_and_scale('images/good/bom.png'),
    load_and_scale('images/bad/alcohol.png'),
    pygame.image.load('images/bad/shouting.png'),
    pygame.image.load('images/bad/fighting.png'),
    load_and_scale('images/bad/phone.png'),
    load_and_scale('images/bad/robbery.png'),
    load_and_scale('images/bad/cigarette.png'),
]


def set_ingredient():
    # Choose a random ingredient
    ingredient = random.choice(ingredientImgs)

    # Tag the ingredient type
    if ingredient in ingredientImgs[-6:]:
        ingredient_type = "bad"
    else:
        ingredient_type = "good"

    x = random.randint(3, 800)  # Random x position across the screen width
    y = random.randint(-200, -50)  # Start above the screen
    speed = random.uniform(3, 8)  # Random speed

    return {"img": ingredient, "x": x, "y": y, "speed": speed, "type": ingredient_type}

def game_over():
    gameOverImg = pygame.image.load('images/game-over.png')
    screen.blit(gameOverImg, (SCREEN_WIDTH // 2 - gameOverImg.get_width() // 2, 120))

    render_score()
    render_prompt2()
    reset_game()

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return  # Exit the game over screen

def reset_game():
    """Reset game state variables and restart background music."""
    global playerX, playerY, playerX_change, count, current_score, hitCount

    # Reset player position and obstacle
    playerX = SCREEN_WIDTH // 2 - playerImg.get_width()//2
    playerY = 550
    playerX_change = 0

    # Reset the score
    count = 0
    hitCount = 0
    current_score = 0

# Player image and positions
playerImg = pygame.transform.scale(pygame.image.load("images/hands.png"),(150,150))
playerX = SCREEN_WIDTH // 2 - playerImg.get_width()//2
playerY = 550
playerX_change = 0

def player(playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))

def main_game():
    global running, playerX, playerY, playerX_change, playerImg, count, current_score, font_path,hitCount
    ingredients = [set_ingredient() for _ in range(5)]

    font_path = 'fonts/ConcertOne-Regular.ttf'

    count = 0
    hitCount = 0
    current_score = 0
    clock = pygame.time.Clock()

    original_player_img = pygame.transform.scale(pygame.image.load("images/hands.png"),(150,150))
    playerImg = original_player_img  # Save the original player image

    while running:
        render_background()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Player movement on key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -8
                elif event.key == pygame.K_RIGHT:
                    playerX_change = 8

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # Draw player
        player(playerX, playerY)

        # Update player position
        playerX += playerX_change

        # Prevent player from moving off screen
        if playerX <= 0:
            playerX = 0
        elif playerX >= SCREEN_WIDTH - playerImg.get_width():
            playerX = SCREEN_WIDTH - playerImg.get_width()
        
        player_rect = pygame.Rect(playerX, playerY, playerImg.get_width(), playerImg.get_height())  # Player's bounding box
        
        # Update and draw each ingredient
        for ingredient in ingredients:
            ingredient["y"] += ingredient["speed"]  # Move ingredient down
            screen.blit(ingredient["img"], (ingredient["x"], ingredient["y"]))

            # Ingredient bounding box
            ingredient_rect = pygame.Rect(
                ingredient["x"], ingredient["y"],
                ingredient["img"].get_width(),
                ingredient["img"].get_height()
            )

            # Check collision
            if player_rect.colliderect(ingredient_rect):
                if ingredient["type"] == "bad":  # Check if bad ingredient
                    count += 1
                    hitCount += 1

                    current_score -= 500

                    if count > 1:
                        if hitCount >= 3:
                            game_over()
                        else:
                            quiz()
                    else:
                        playerImg = pygame.transform.scale(pygame.image.load("images/hands-2.png"),(150,150))  # Change player image
                        player(playerX, playerY)
                        pygame.display.update()
                        pygame.time.delay(500)  # Show the new image for 0.5 seconds
                        playerImg = original_player_img  # Restore original image
                
                if ingredient["type"] == "good":
                    current_score +=200

                # Remove collided ingredient and spawn a new one
                ingredients.remove(ingredient)
                ingredients.append(set_ingredient())

            # Reset ingredient if it falls below the screen
            if ingredient["y"] > SCREEN_HEIGHT:
                ingredients.remove(ingredient)
                ingredients.append(set_ingredient())

        current_score += 1
        scoreCard = pygame.image.load('images/score-card.png')
        screen.blit(scoreCard, (10,10))
        font = pygame.font.Font(font_path, 40)
        score_text = font.render(f"Score: {current_score}", True, black)
        screen.blit(score_text, (32, 30))

        pygame.display.update()
        clock.tick(60)

while running:
    title_screen()
    instructions()
    if running:  
        main_game()
pygame.quit()