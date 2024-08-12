# Tutorial: https://pygame-zero.readthedocs.io/en/stable/introduction.html
import pgzrun  # program must always start with this
from platformer import *
from pgzhelper import  *

# Pygame constants
WIDTH = 800
HEIGHT = 600
TITLE = "Platformer"

# global variables
jump_velocity = -10
gravity = 1
win = False
over = False

# define Sprites
# Sprite("sprite_image.png", start, num_frames, color_key, refresh)
color_key = (0, 0, 0)  # leave like this unless background shows up
player_idle = Sprite("player.png", (0, 48, 48, 48), 6, color_key, 5)
player_walk = Sprite("player.png", (0, 4 * 48, 48, 48), 6, color_key, 5)

# define SpriteActor
player = SpriteActor(player_idle)
player.bottomleft = (0, HEIGHT - 35)
# define Actor-specific variables
player.alive = True
player.jumping = False
player.velocity_x = 3
player.velocity_y = 0

platforms = Actor("button_start")
platforms.pos = (0,HEIGHT)


# displays the new frame
def draw():
    screen.clear()  # clears the screen
    screen.fill("skyblue")  # fills background color
    # draw the player if still alive
    if player.alive:
        player.draw()
        platforms.draw()

    # draw messages over top
    if over:
        screen.draw.text("Game Over", center=(WIDTH / 2, HEIGHT / 2))
    if win:
        screen.draw.text("You win!", center=(WIDTH / 2, HEIGHT / 2))# Escreva o seu código aqui :-)


def update():
    # declare scope of global variables
    global win, over

    # if game is over, no more updating game state, just return
    if over or win:
        return

    # handle player left movement
    if keyboard.LEFT and player.left > 0:
        player.x -= player.velocity_x
        # flip image and change sprite
        player.sprite = player_walk
        player.flip_x = True
                    # get object that playercollided with
            collided = player.collidelist(platforms)]
            # use it to calculate position where there is no collision
            player.left = collided.right

    elif keyboard.RIGHT and player.right < WIDTH:
        player.x += player.velocity_x
        # flip image and change sprite
        player.sprite = player_walk
        player.flip_x = False

        # handle gravity
    player.y += player.velocity_y
    player.velocity_y += gravity


# keyboard pressed event listener
    def on_key_down(key):
        # up key and not already jumping
        if key == keys.UP and not player.jumping:
            player.velocity_y = jump_velocity
            player.jumping = True


    # called when a keyboard button is released
    def on_key_up(key):
        # change to forward facing image when left/right keys released
        if key == keys.LEFT or key == keys.RIGHT:
            player.sprite = player_idle
