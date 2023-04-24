import pygame 
import math

pygame.init()

run = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1150,700))
pygame.display.set_caption('Dodge This')

#organize animations
player_animation = []
player_idle = []
player_jump = []
player_stayjump = []
player_fallingdown = []

#enemy animations
blob = []
#enemy clips
enemy_clips = 0

for i in range (0,8):
    player_animation.append(pygame.image.load(f'animation/alien_run{i}.png').convert_alpha())
    player_idle.append(pygame.image.load(f'animation/alien_run{i}.png').convert_alpha())
for i in range (0,14):
    player_jump.append(pygame.image.load(f'animation/jump/alien_jump0{i}.png').convert_alpha())
for i in range(0,11):
    player_stayjump.append(pygame.image.load(f'animation/stayjump/alien_stay_jump0{i}.png').convert_alpha())
for i in range(0,8):
    player_fallingdown.append(pygame.image.load(f'animation/fallingdown/alien_fallingdown{i}.png').convert_alpha())
for i in range(0,4):
    blob.append(pygame.image.load(f'animation/blob{i}.png').convert_alpha())

first_clip = 0
first_clipidle = 0
first_clipjump = 0
first_clipfalling = 0
#cooldown and update time
cooldown = 100
update_time = 0
#enemy
enemy_cooldown = 60
enemy_update_time = 0

#starting position
x = 50
y = 450
#enemy position
enemy_x = 1140
enemy_y = 430

#physics
gravity = 3
jump_gravity = 4
j = False
#player

#text
home = pygame.font.Font(None, 50)
score = pygame.font.Font(None, 50)
play = False
start = False
game_over = False
counter = 0

def idle():
    global j, update_time, first_clip, player_animation, player_fallingdown, first_clipfalling, first_clipidle, first_clipjump, y, gravity, jump_gravity
    if not key[pygame.K_SPACE] and j == False:
        player_animation = player_idle
        first_clipfalling = 0
        first_clip = first_clipidle
        first_clipjump = 0
        if pygame.time.get_ticks()-update_time > cooldown:
            first_clipidle += 1
            update_time = pygame.time.get_ticks()
            if first_clipidle == 7:
                first_clipidle = 0

    elif not key[pygame.K_SPACE] and j == True:
        player_animation = player_fallingdown
        first_clip = first_clipfalling
        first_clipidle = 0
        y += gravity
        if pygame.time.get_ticks() - update_time > cooldown:
            first_clipfalling += 1
            update_time = pygame.time.get_ticks()
        if first_clipfalling == 7:
            first_clipfalling = 5
        if y >= 450:
            j = False
            y = 450

def jump():
    global current_animation, update_time, first_clip, player_animation, player_stayjump, j, first_clipjump, y, jump_gravity, first_clipidle, first_clipfalling
    if key[pygame.K_SPACE]:
        j = True
        player_animation = player_jump + player_stayjump
        first_clip = first_clipjump
        y -= jump_gravity
        if j == True:
            if pygame.time.get_ticks()-update_time > cooldown:
                first_clipjump += 1
                update_time = pygame.time.get_ticks()
            if first_clipjump == 23:
                first_clipjump = 14

def enemy():
    global enemy_update_time, enemy_clips, enemy_x, enemy_cooldown, counter
    enemy_x -=7
    if enemy_x < -150:
        enemy_x = 1200
        counter +=1
    if pygame.time.get_ticks() - enemy_update_time > enemy_cooldown:
        enemy_clips += 1
        enemy_update_time = pygame.time.get_ticks()
    if enemy_clips == 3:
        enemy_clips = 0

while run:
    clock.tick(60)
    screen.fill('white')
    if not play and not start:
        key = pygame.key.get_pressed()
        home_surf = home.render('Ready? Press Space to play.', False, 'Black')
        screen.blit(home_surf, (360, 300))
        if key[pygame.K_SPACE]:
            play = True
            start = True
    elif play:
        #initialize key
        key = pygame.key.get_pressed()
        #player
        current_animation = player_animation[first_clip]
        idle()
        jump()
        #rectangle
        anim_rect = current_animation.get_rect(center = (x, y))
        #enemy
        enemy_animation = blob[enemy_clips]
        enemy_rect = enemy_animation.get_rect(center = (enemy_x, enemy_y))
        enemy()
        #screen display
        screen.blit(current_animation, anim_rect)
        screen.blit(enemy_animation, enemy_rect)
        #score
        score_surf = score.render(f'{counter}', False, 'Black')
        screen.blit(score_surf, (435, 50))
        if anim_rect.colliderect(enemy_rect):
            play = False
    elif not play and start:
        key = pygame.key.get_pressed()
        home_surf = home.render('Game over.', False, 'Black')
        screen.blit(home_surf, (575, 350))
        if key[pygame.K_RETURN]:
            enemy_x = 1140
            start = False
            counter = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
