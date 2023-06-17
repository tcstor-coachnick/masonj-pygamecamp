import pygame
import random

class Enemy:
    def __init__(self, image):
        self.x = random.randint(0, 1000)
        self.y = random.randint(0, 1000)
        self.image = image
        self.width = 150
        self.height = 150
        self.hp = 30
        self.damage = 1

def iscolliding(thing):
    if thing.y > (y + height):
        return False
    elif (thing.y + thing.height)< y:
        return False
    if thing.x > (x + height):
        return False
    elif (thing.x + thing.width)< x:
        return False
    return True
    
def loadimage(path):
    image = pygame.image.load(path) 
    image = pygame.transform.scale(image, (150, 150))
    return image    

pygame.init()
window = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("shooter reloader")
clock= pygame.time.Clock()
standing = pygame.image.load("shooter reloader/mason going left 1.png")
standing = pygame.transform.scale(standing, (150, 150))
walkingleft = [loadimage("shooter reloader/mason going left 1.png"), loadimage("shooter reloader/mason going left 2.png")]
walkingup =  [loadimage("shooter reloader/mason going up 1.png"), loadimage("shooter reloader/mason going up 2.png")]
walkingdown = [loadimage("shooter reloader/mason going down 1.png"), loadimage("shooter reloader/mason going down 2.png")]
walkingright = [loadimage("shooter reloader/mason going right 1.png"), loadimage("shooter reloader/mason going right 2.png")]
shootingup = [loadimage("shooter reloader/mason shooting up.png"), loadimage("shooter reloader/mason shooting up.png")]
shootingright = [loadimage("shooter reloader/mason shooting right.png"), loadimage("shooter reloader/mason shooting right.png")]
shootingdown = [loadimage("shooter reloader/mason shooting down.png"), loadimage("shooter reloader/mason shooting down.png")]
shootingleft = [loadimage("shooter reloader/mason shooting left.png"), loadimage("shooter reloader/mason shooting left.png")]
sandenemy = [loadimage("shooter reloader/sand enemy 1.png"), loadimage("shooter reloader/sand enemy 2.png"),loadimage("shooter reloader/sand enemy 3.png"), loadimage("shooter reloader/sand enemy 3.png")]
shootingstanding = [loadimage("shooter reloader/mason shooting left.png"), loadimage("shooter reloader/mason shooting left.png")]
dead = [loadimage("shooter reloader/death animation1.png"), loadimage("shooter reloader/death animation 2.png"), loadimage("shooter reloader/death animation 3.png"), loadimage("shooter reloader/death animation 4.png"), loadimage("shooter reloader/death animation 5.png")]
# x is left and right
x = 0
# y is up and down
y = 0
width = 150
height = 150
speed = 5
hp = 100
damage = 20
direction = "left"
framenumber = 0
enemies = []
attacking = False
death = False
run = True
while run:
    clock.tick(40)
    if death:
        window.fill((204, 170, 0))
        window.blit(dead[framenumber//8], (x, y))
        pygame.display.update()
        if framenumber == 39:
            pygame.time.delay(100)
            break
        else:
            framenumber += 1
            continue
    framenumber += 1
    if framenumber == 1:
        enemy = Enemy(sandenemy)
        enemies.append(enemy)
    if framenumber == 23:
        framenumber = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    attacking = False
    direction = "none"
    if keys [pygame.K_RIGHT]:
        standing = loadimage("shooter reloader/mason going right 1.png")
        x += speed
        direction = "right"
        shootingstanding = [loadimage("shooter reloader/mason shooting right.png"), loadimage("shooter reloader/mason shooting right.png")]
    if keys[pygame.K_LEFT]:
        standing = loadimage("shooter reloader/mason going left 1.png")
        x -= speed
        direction = "left"
        shootingstanding = [loadimage("shooter reloader/mason shooting left.png"), loadimage("shooter reloader/mason shooting left.png")]
    if keys[pygame.K_UP]:
        standing = loadimage("shooter reloader/mason going up 1.png")
        y -= speed
        direction = "up"
        shootingstanding = [loadimage("shooter reloader/mason shooting up.png"), loadimage("shooter reloader/mason shooting up.png")]
    if keys[pygame.K_DOWN]:
        standing = loadimage("shooter reloader/mason going down 1.png")
        y += speed
        direction = "down"
        shootingstanding = [loadimage("shooter reloader/mason shooting down.png"), loadimage("shooter reloader/mason shooting down.png")]
    if keys[pygame.K_SPACE]:
        attacking = True
    
    window.fill((204, 170, 0))
    #pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    if attacking:
        if direction == "right":
            window.blit(shootingright[framenumber//12],(x, y))
        if direction == "left":
            window.blit(shootingleft[framenumber//12],(x, y))
        if direction == "up":
            window.blit(shootingup[framenumber//12],(x, y))
        if direction == "down":
            window.blit(shootingdown[framenumber//12],(x, y))
        if direction == "none":
            window.blit(shootingstanding[framenumber//12],(x, y))
    elif direction == "left":
        window.blit(walkingleft[framenumber // 12], (x, y))
    elif direction == "up":
        window.blit(walkingup[framenumber //12], (x, y))
    elif direction == "down":
        window.blit(walkingdown[framenumber //12], (x, y))
    elif direction == "right":
        window.blit(walkingright[framenumber //12], (x, y))
    else:
        window.blit(standing, (x, y))
    for enemy in enemies:
        window.blit(enemy.image[framenumber//8], (enemy.x, enemy.y))
        if iscolliding(enemy):
            if attacking:
                enemy.hp -= damage
                if enemy.hp < 1:
                    enemies.remove(enemy)
            else:
                hp -= enemy.damage
                if hp < 1:
                    death = True
                    framenumber = 0
    pygame.display.update()
pygame.quit()