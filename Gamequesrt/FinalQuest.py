# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 1
# Video link: https://www.youtube.com/watch?v=nGufy7weyGY
# Player sprite and movement

import pygame as pg
from pygame.sprite import Sprite
import random
from os import path
#Scoreboard Font
import pygame.font

#Game Dimensions
#Width of screen
WIDTH = 480
#height of screen
HEIGHT = 600
#Frames Per Second
FPS = 60
score = 0

# define colors
WHITE = (255, 255, 255)
DARKBLUE = (39, 54, 77)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

font_name = pg.font.match_font('arial')
game_dir = path.join(path.dirname(__file__))
#Load images onto game
background_image = pg.image.load(game_dir + "/img/bg.png")
background_rect = background_image.get_rect()
background_rect2 = background_image.get_rect()
player_image = pg.image.load(game_dir + "/img/player.png")
mob_image = pg.image.load(game_dir + "/img/mob.png")

# initialize pygame...
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
#Presents title of the game
pg.display.set_caption("Space Crusaders")
clock = pg.time.Clock()

# utils

# Prepares font "Arial" for use
font_name = pg.font.match_font('arial')

# the following function allows us to draw text on the screen
def draw_text(surf, text, size, x, y):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

#All classes are below
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        #Image size
        self.image = pg.Surface((50,40))
        #Color
        self.image.fill(GREEN)
        #Places image
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        #Player Health
        self.hitpoints = 100
        #Ammo total
        self.ammo = 100
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_w]:
            self.pew()
        if keystate[pg.K_a]:
            self.speedx = -8
        if keystate[pg.K_d]:
            self.speedx = 8
        # if keystate[pg.K_w]:
        #     self.speedy = -8
        # if keystate[pg.K_s]:
        #     self.speedy = 8
        self.rect.x += self.speedx
        self.rect.y += self.speedy
    def pew(self):
        if self.ammo > 0:
            lazer = Lazer(self.rect.centerx, self.rect.top)
            all_sprites.add(lazer)
            lazers.add(lazer)
            self.ammo-=1
            # print(self.ammo)

class Mob(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        #Image size
        self.image = pg.Surface((40,40))
        #Color
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH-self.rect.width)
        self.rect.y = random.randrange(0, 240)
        self.speedx = random.randrange(1,10)
        self.speedy = random.randrange(1,10)
    #Update mob and Mob Boundaries
    def update(self):
        self.rect.x += self.speedx
        if self.rect.x > WIDTH or self.rect.x < 0:
            self.speedx*=-1
            self.rect.y += 25
        if self.rect.y > HEIGHT:
            self.rect.y = -25
            self.rect.x = random.randrange(0, WIDTH-self.rect.width)
class Lazer(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        #Image size
        self.image = pg.Surface((5,25))
        #Color associated with class
        self.image.fill(BLUE)
        #Image Placement
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        #When Player health reaches 0 they are killed
        if self.rect.bottom < 0:
            self.kill()
#Class to report scoring info


#Assisted by Python Crash Course Textbook
#attempted to add a scoreboard
class Scoreboard(Sprite):
    #initialize scorekeeping 
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #Font/ Text color
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(none, 48)

        #Preparation for initial score image
        self.prep_score()
    #turn text to be displayed into an image
    def prep_score(self):
        #turns the score into a rendered image
        score_str = str(self.stats.score)
        #Sets score on the background
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        #displays score at top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    #displays rendered scoreboard 
    def show_score(self):
        #Draws score on screen
        self.screen.blit(self.score_image, self.score_rect)

    def initialize_dynamic_settings(self):
        #scoring
        self.Mob_points = 50
    
    def check_Lazer_Mob_collisions(self, ai_settings, screen, stats, sb, Player, Mob, Lazer):
        #Respond to Mob-Lazer collisions
        #Removes Lazers and ALiens that have collided
        collisions = pygame.sprite.groupcollide(Lazer, Mob, True, True)
        if collisions:
            stats.score += ai_settings.Mob_points
            sb.prep_score
    def update_Lazer(self, ai_settings, screen, stats, sb, Player, Mob, Lazer):
        #update lazer position remove old lazers
        self.check_Lazer_Mob_collisions(ai_settings, screen, stats, sb, Player, Mob, Lazer)
    
   






# where classes get created and added to sprites group
all_sprites = pg.sprite.Group()
#added scoreboard to sprite group
Scoreboard = pg.sprite.Group()
mobs = pg.sprite.Group()
lazers = pg.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(0,8):
    mob = Mob()
    all_sprites.add(mob)
    mobs.add(mob)


# the game loop
running = True
while running: 
    # keep loop running based on clock
    clock.tick(FPS)
    for event in pg.event.get():
        # window x button
        if event.type == pg.QUIT:
            running = False

    # update
    all_sprites.update()
    #If mobs and Lazers collide with other classes they no longer can run
    hits = pg.sprite.groupcollide(mobs, lazers, True, True)
    hits = pg.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False
    
    if len(mobs) == 0:
        for i in range(0,8):
            mob = Mob()
            all_sprites.add(mob)
            mobs.add(mob)

#colors screen
screen.fill(DARKBLUE)
#adds custom image to background
screen.blit(background_image, background_rect)
screen.blit(background_image, background_rect2)
draw_text(screen, str(score), 24, WIDTH / 2, 10)
draw_text(screen, str(player.ammo), 24, WIDTH / 4, 10)
draw_text(screen, str(player.hitpoints), 16, player.rect.x, player.rect.y)

all_sprites.draw(screen)
pg.display.flip()


pg.quit()