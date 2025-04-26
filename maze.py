#создай игру "Лабиринт"!
from pygame import *
init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        if keys_pressed[K_LEFT]  and self.rect.x > 2:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT]  and self.rect.x < 635:
            self.rect.x += self.speed
        if keys_pressed[K_UP]  and self.rect.y > 2:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN]  and self.rect.y < 435:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.direction = 'left'
    def update(self):
        if self.rect.x <= 450:
            self.direction = 'right'
        if self.rect.x >= 600:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.height = wall_height
        self.width = wall_width
        self.image = Surface((self.width, self.height))
        self.image.fill((self.color1, self.color2, self.color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
             
window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
Background = transform.scale(image.load('background.jpg'), (700, 500))
sprite1 = Player('hero.png', 50, 400, 4)
sprite2 = Enemy('cyborg.png', 600, 300, 2)
sprite3 = GameSprite('treasure.png', 570, 420, 0)
sprite4 = Enemy('cyborg.png', 500, 170, 2)
wall1 = Wall(202, 142, 66, 150, 470, 290, 10)
wall2 = Wall(202, 142, 66, 430, 120, 10, 350)
wall3 = Wall(202, 142, 66, 150, 365, 200, 10)
wall4 = Wall(202, 142, 66, 150, 0, 10, 365)
wall5 = Wall(202, 142, 66, 240, 275, 200, 10)
wall6 = Wall(202, 142, 66, 150, 190, 200, 10)
wall7 = Wall(202, 142, 66, 240, 110, 200, 10)
game = True
clock = time.Clock()
FPS = 60
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.05)
mixer.music.play()
money_sound = mixer.Sound('money.ogg')
money_sound.set_volume(0.05)
kick_sound = mixer.Sound('kick.ogg')
kick_sound.set_volume(0.09)
main_font = font.SysFont('Comic Sans MS', 70)
finish = False
win = main_font.render('You Win', True, (241, 207, 59))
louse = main_font.render('Game Over', True, (241, 36, 0))
while game:
    if finish != True:
        keys_pressed = key.get_pressed()
        window.blit(Background,(0, 0))
        sprite1.reset()
        sprite2.reset()
        sprite3.reset()
        sprite4.reset()
        sprite1.update()
        sprite2.update()
        sprite4.update()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        if sprite.collide_rect(sprite1, sprite3):
            finish = True
            money_sound.play()
            window.blit(win, (200, 200))
        if sprite.collide_rect(sprite1, wall1) or sprite.collide_rect(sprite1, wall2) or sprite.collide_rect(sprite1, wall3) or sprite.collide_rect(sprite1, wall4) or sprite.collide_rect(sprite1, wall5) or sprite.collide_rect(sprite1, wall6) or sprite.collide_rect(sprite1, wall7):
            sprite1.rect.x = 50
            sprite1.rect.y = 400
            kick_sound.play()
        if sprite.collide_rect(sprite1, sprite2) or sprite.collide_rect(sprite1, sprite4):
            finish = True
            kick_sound.play()
            window.blit(louse, (200, 200))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
    