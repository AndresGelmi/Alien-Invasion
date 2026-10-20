import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from time import sleep
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    def __init__(self):
        pygame.init()
        #Iniciar el módulo
        
        self.settings = Settings()
        #Crea una instancia de los "settings"
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #Crea una pantalla
        
        self.ship = Ship(self)
        #Crea una nave
        
        self.bullets = pygame.sprite.Group()
        #Crea el conjunto de balas
        
        self.aliens = pygame.sprite.Group()
        alien = Alien(self)
        alien.rect.y += 30
        
        self.button = Button(self,"Play")
        
        self.game_stats = GameStats(self)
        self.game_active = False
        
        self.sb = Scoreboard(self)
        
        self.aliens.add(alien)
        pygame.display.set_caption("Alien Invasion")
        #Le da un título
        
        self.clock = pygame.time.Clock()

        #Crea un temporizador
       
        
        
        self._create_fleet()
        

            
    def _check_events(self): 
        #Chequea eventos
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                    
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_mouse(mouse_pos)
                    
                    
    def _check_keydown_events(self,event):
        #Chequea eventos de apretar teclas
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
            
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True 
        
        elif event.key == pygame.K_q:
            sys.exit()
            
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_keyup_events(self,event):
        #Chequea eventos de liberacion de teclas
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
            
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _update_screen(self):
        #Actualiza la pantalla
        self.screen.fill(self.settings.bg_color)
        self.sb.draw_scoreboard()
        self.sb.show_level()
        #self.stars.draw(self.screen)        
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        if not self.game_active:
            self.button.draw_button()
        
        pygame.display.flip()
    def _check_mouse(self,mouse_pos):
        button_clicked = self.button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            if self.game_stats.score > self.sb.high_score:
                self.sb.high_score = self.game_stats.score
            self.game_stats.reset_stats()
            self.sb.prep_msg()
            self.sb.prep_high_score()
            self.sb.prep_level()
            self.game_active = True
            self.game_stats.reset_stats()
            self.bullets.empty()
            self.aliens.empty()
            

            
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)
            self.settings._initialize_dynamic_factors()
            sleep(0.5)
        
    def _fire_bullet(self):
        #Dispara balas
        if len(self.bullets)  < self.settings.bullets_allowed:
            
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        
        self.bullets.update()
        #Elimina las balas que se salen del mapa
        for bullet in self.bullets.copy():
                if bullet.rect.bottom  <= 0:
                    self.bullets.remove(bullet)
                    print(len(self.bullets))
        
        self._check_alien_bullet_collisions()
        
    def _check_alien_bullet_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collisions:
            for alien in collisions.values():
                self.game_stats.score += self.settings.alien_points * len(alien)
            self.sb.prep_msg()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.game_stats.current_level += 1
            self.sb.prep_level()
            
            
                  
    def _create_fleet(self):
        
        alien = Alien(self)
        
        alien_width,alien_height = alien.rect.size
        current_x,current_y = alien_width,alien_height
        while current_y <(self.settings.screen_width - 20* alien_height):
            while current_x <(self.settings.screen_width - 2* alien_width):
                self._create_alien(current_x,current_y)
                current_x += 2*alien_width
            current_x = alien_width
            current_y += 2 * alien_height
    def _create_alien(self,x_position,y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.y = y_position + 30
        new_alien.rect.x = new_alien.x
        self.aliens.add(new_alien)
        
    def _update_aliens(self):
        self._check_fleet_edges()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        self._check_alien_bottom()
        self.aliens.update()
        
        
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
                
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.alien_direction *= -1
            
    def _ship_hit(self):
        if self.game_stats.ship_left > 0:
            self.game_stats.ship_left -= 1
            self.sb.prep_ship()
        
            self.bullets.empty()
            self.aliens.empty()
            
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

        
    def _check_alien_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break
            
    
    def run(self):
        while True:
            
            self._check_events()
            if self.game_active:
                self._update_bullets()
                self.ship.update()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)
            
    
ai = AlienInvasion()
ai.run()
        