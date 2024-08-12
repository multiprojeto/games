import pgzrun

WIDTH = 500
HEIGHT = 520

alien = Actor('blank')
alien.pos = 100, 56

botao = Actor('button_start')
botao.pos = WIDTH / 2 , HEIGHT / 2



def draw():
    screen.clear()
    screen.blit("background", (0, 0))
    alien.draw()
    botao.draw()

def update():

    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0
    if keyboard.up:
        alien.y -= 2
    if keyboard.down:
        alien.y += 2
    if alien.y < 20:
        alien.y = 20
    if alien.y > 520:
        alien.y = 520

def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)

def on_mouse_down(pos):
    if botao.collidepoint(pos):
        set_alien_hurt()


def set_alien_hurt():
    alien.image = 'alien_hurt'
    botao.image = 'blank'
    sounds.eep.play()


def set_alien_normal():
    alien.image = 'blank'


pgzrun.go()
