import pygame
from random import randint

path = "C:\\Users\\bartl\\Documents\\Snake Score Saves\\"
running = True
(width, height, bg_colour) = (1000, 700, (0, 0, 0))
(velx, vely, scl) = (10, 0, 10)

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

def saveScore(path):
    print(f"Your score is {len(snake.length)}")
    savescore = open(path + str(len(snake.length)), "w")
    savescore.close()

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = ["_"]
        self.positions = [[30, 350]]
    def draw(self):
        for i in range(len(self.length)):
            pygame.draw.rect(screen, (255, 255, 255), (self.positions[-i - 1][0], self.positions[-i - 1][1], scl, scl))
    def update(self):
        self.x += velx
        self.y += vely
        self.positions.append([self.x, self.y])
    def minimizepositions(self):
        while True:
            if len(self.positions) > len(self.length):
                self.positions.pop(0)
            if len(self.positions) == len(self.length):
                break
            
    def collidecheck(self):
        if self.x > width or self.x < 0 or self.y < 0 or self.y > height:            print("You hit a wall!")
            saveScore(path)
            running = False
            pygame.display.quit()
        for i in range(len(self.positions)):
            if (self.x + velx) == self.positions[i][0] and (self.y + vely) == self.positions[i][1]:
                print("You hit yourself")
                saveScore(path)
                running = False
                pygame.display.quit()

class Food:
    def __init__(self):
        self.x = randint(0, width/scl) * scl
        self.y = randint(0, height/scl) * scl
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, scl, scl))
    def update(self):
        if snake.x == self.x and snake.y == self.y:
            self.x = randint(0, width/scl) * scl
            self.y = randint(0, height/scl) * scl
            snake.length.append("_")
            
snake = Snake(30, 350)
food = Food()

while running:
    try:
        clock.tick(10)
        screen.fill(bg_colour)

        food.draw()
        food.update()
        snake.minimizepositions()
        snake.draw()
        snake.update()
        snake.collidecheck()
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                saveScore(path)
                pygame.display.quit()
                running = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if vely != -scl or vely != scl:
                        vely = -scl
                        velx = 0
                if event.key == pygame.K_s:
                    if vely != -scl or vely != scl:
                        vely = scl
                        velx = 0
                if event.key == pygame.K_a:
                    if velx != -scl or velx != scl:
                        vely = 0
                        velx = -scl
                if event.key == pygame.K_d:
                    if velx != -scl or velx != scl:
                        vely = 0
                        velx = scl
    except:
        pass
                

