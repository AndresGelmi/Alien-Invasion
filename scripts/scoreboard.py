import pygame.font
from ship import Ship
from pygame.sprite import Group

class Scoreboard:
    def __init__(self,game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.stats = game.game_stats
        
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        
        self.high_score = 0
        
        self.prep_msg()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()
    def prep_msg(self):
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True,
            self.text_color, self.settings.bg_color)   
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def draw_scoreboard(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.ships.draw(self.screen)
        
    def prep_high_score(self):
        
        high_score = round(self.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.settings.bg_color)  
        
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    def prep_level(self):
        level_str = str(self.stats.current_level)
        self.level_image = self.font.render(level_str, True,
            self.text_color, self.settings.bg_color)   
        
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    def show_level(self):
        self.screen.blit(self.level_image,self.level_rect)
        
    def prep_ship(self):
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship_size = (50, 50)  # Define el nuevo tamaño aquí
            ship = Ship(self.game, ship_size)  # Pasa el tamaño como argumento
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
        