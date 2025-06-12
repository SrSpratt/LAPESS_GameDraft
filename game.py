import pygame

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display
        self.window = self.screen.set_mode((width, height))
        self.screen.set_caption("Pule e pegue o maior quadrado!")
        self.colors = {
            "white" : (255, 255, 255),
            "black" : (0, 0, 0),
            "green" : (100, 255, 0),
            "red" : (255, 0, 100),
            "blue" : (0, 0, 255)
        }
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.font = pygame.font.SysFont(None, 36)
        self.gravity = 1
        self.arrow_map = {
            pygame.K_SPACE : "up",
            pygame.K_LEFT : "left",
            pygame.K_RIGHT : "right"
        }
    
    def draw(self):
        platform_y_pos = self.height - 50
        player_y_pos = platform_y_pos - 50
        self.platform = pygame.Rect(0, platform_y_pos, 600, 20)
        self.player = Player(400, player_y_pos, 50, 50)
    
    def spawn(self):
        a = "a"
    
    def loop(self):
        score = 0
        rounds = 0
        max_rounds = 10
        running = True
        
        while running:
            self.clock.tick(self.FPS)
            self.window.fill(self.colors["white"])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                self.player.move("up")
            if key[pygame.K_LEFT] and self.player.me.x >= 0:
                self.player.move("left")
            if key[pygame.K_RIGHT] and self.player.me.x + self.player.me.width <= self.width:
                self.player.move("right")
            self.player.fall(self.platform.y, self.gravity)
            pygame.draw.rect(self.window, self.colors["blue"], self.player.me)
            pygame.draw.rect(self.window, self.colors["green"], self.platform)
            pygame.display.update()
        pygame.quit()
    
class Player:
    def __init__(self, pos_x, pos_y, width, height):
        self.me = pygame.Rect(pos_x, pos_y, width, height)
        self.vel_x = 5
        self.vel_y = 0
        self.jumping = False
    
    def move(self, event):
        if event == "up" and not self.jumping:
            self.jumping = True
            self.vel_y = -15
        if event == "left":
            self.me.x -= self.vel_x
        if event == "right":
            self.me.x += self.vel_x
        
    
    def fall(self, surface, gravity):
        if self.jumping:
            self.me.y += self.vel_y
            self.vel_y += gravity
            if self.me.y >= surface - self.me.height:
                self.me.y = surface - self.me.height
                self.vel_y = 0
                self.jumping = False


if __name__ == "__main__":
    game = Game(600, 400)
    game.draw()
    game.loop()


