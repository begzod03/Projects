import pygame, sys, random

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos, 640))
    screen.blit(floor_surface,(floor_x_pos + 400, 640))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (450, random_pipe_pos)) #placing our pipe in the middle of the map (bottom)
    top_pipe = pipe_surface.get_rect(midbottom = (450, random_pipe_pos - 200)) # placing our pipe from top
    return bottom_pipe, top_pipe # we are returning tuple, so we have to extend rather append our list

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 700:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True) #built in function pygame.transform.flip flips given content (what, x, y)
            screen.blit(flip_pipe, pipe)

def move_pipes(pipes): # this functions takes all the pipes abd move them to the left by 5 pixels
    for pipe in pipes:
            pipe.centerx -=2
    return pipes

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe): # this checks if the birds rectangle collides with the pipe rect, the function is colliderect
            hit_sound.play()
            return False
        if bird_rect.top <= -100 or bird_rect.bottom >= 640:
            hit_sound.play()
            return False

    return True

def rotate_bird(bird): # this is the function that rotates the bird
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
    return new_bird, new_bird_rect

def score_display(game_state):
    if game_state == "main_game":
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255)) #this is the appearance of the text, True is to make the text sharper(does not mattter that much)
        score_rect = score_surface.get_rect(center = (200, 100))
        screen.blit(score_surface, score_rect)

    if game_state == "game_over":
        high_score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))  # this is the appearance of the text, True is to make the text sharper(does not mattter that much)
        high_score_rect = high_score_surface.get_rect(center=(200, 110))
        screen.blit(high_score_surface, high_score_rect)

        high_score_surface = game_font.render(f'High score: {int(high_score)}', True, (255, 255,255))  # this is the appearance of the text, True is to make the text sharper(does not mattter that much)
        high_score_rect = high_score_surface.get_rect(center=(200, 550))
        screen.blit(high_score_surface, high_score_rect)

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

pygame.init()
screen = pygame.display.set_mode((392, 700)) #Creates the canvas in the format of 576x700
clock = pygame.time.Clock() #This is used to limit our frmate rate
game_font = pygame.font.Font("04B_19.ttf" ,40)# this creates the font for our text (font-style, font-size)


# Game Variables
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0


bg_surface = pygame.image.load('assets/background-day.png').convert() #making a variable for surface (method)

floor_surface = pygame.image.load("assets/base.png").convert()
floor_x_pos = 0

#animation

bird_downflap = pygame.image.load("assets/bluebird-downflap.png")
bird_midflap = pygame.image.load("assets/bluebird-midflap.png")
bird_upflap = pygame.image.load("assets/bluebird-upflap.png")
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100, 350))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200) # this changes bird_index every 200 milliseconds

#bird_surface = pygame.image.load("assets/bluebird-midflap.png")
#bird_rect = bird_surface.get_rect(center = (100, 350)) #this takes bird surface and puts a rectangle around it(for collision)

pipe_surface = pygame.image.load("assets/pipe-green.png")
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200) #1200 is in milliseconds, so this is 1.2 seconds
pipe_height = [300, 400, 600]

game_over_surface = pygame.image.load("assets/message.png")
game_over_rect = game_over_surface.get_rect(center = (200, 350))

# making sound stuff with pygame.mixer
flap_sound = pygame.mixer.Sound("sound/sound_sfx_wing.wav")
hit_sound = pygame.mixer.Sound("sound/sound_sfx_hit.wav")
point_sound = pygame.mixer.Sound("sound/sound_sfx_point.wav")
death_sound = pygame.mixer.Sound("sound/sound_sfx_die.wav")

score_sound_countdown = 100


while True:
    for event in pygame.event.get(): #pygame is looking for all the events that are happening right now
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE  and game_active:
                bird_movement = 0
                bird_movement -= 6
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False: # this is what happens when we die

                game_active = True # everything happening after this is what happens when we respawn
                pipe_list.clear()
                bird_rect.center = (100, 350 )
                bird_movement = 0
                score = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe()) # stores each pipe in our list

        if event.type == BIRDFLAP:
            if bird_index > 2:
                bird_index += 1
            else:
                bird_index = 0

            bird_surface, bird_rect = bird_animation()

    screen.blit(bg_surface,(0,0)) #this put one surface on another

    if game_active:


        #bird
        bird_movement += gravity #this is what makes the bird have gravity impact
        rotated_bird = rotate_bird(bird_surface) # this makes the bird rotate and look down after a jump
        bird_rect.centery += bird_movement # this is what make the bird fall down
        screen.blit(rotated_bird,bird_rect)
        game_active = check_collision(pipe_list)


        #Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        score += 0.01
        score_display("main_game")
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            point_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display("game_over")


    #Floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -400:
        floor_x_pos = 0




    pygame.display.update()#refreshes the screen
    clock.tick(120) #This is the fps we are are limiting the game with(max fps)
