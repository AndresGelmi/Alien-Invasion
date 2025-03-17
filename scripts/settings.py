class Settings:
    def __init__(self):
        self.screen_height = 600
        #Altura de la pantalla

        self.screen_width = 900
        #Largo de la pantalla
        
        self.bg_color = (230,230,230)
        #Color de la pantalla
        
       
        #Velocidad de la nave
        
        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 5
        
        self.ship_limit = 3
        self.game_speed_up = 1.1
        self.alien_points = 50
        
        self._initialize_dynamic_factors()
        
        self.alien_drop_speed = 10
        
        self.score_scale = 1.5
        
    
    def _initialize_dynamic_factors(self):
        self.bullet_speed = 5.0
        self.alien_speed = 1.0
        self.speed = 5
        self.alien_direction = 1
        
    def increase_speed(self):
        self.bullet_speed *= self.game_speed_up
        self.alien_speed *= self.game_speed_up
        self.speed *= self.game_speed_up
        
        self.alien_points = int(self.alien_points * self.score_scale)