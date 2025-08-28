import pygame
import random
from code.Const import WHITE, HEIGHT, WIDTH
from code.EntityFactory import EntityFactory
from code.Bullet import Bullet
from code.Enemy import Enemy
from code.Player import Player
from code.Explosion import Explosion  # Sua classe de explosão

class Level:
    def __init__(self, window, name, difficulty):
        self.window = window
        self.name = name
        self.bg_layers = EntityFactory.get_backgrounds()
        self.clock = pygame.time.Clock()

        # Inicializar mixer e sons

        self.shoot_sound = pygame.mixer.Sound("./assets/lasersfx.ogg")
        self.shoot_sound.set_volume(0.3)
        self.explosion_sound = pygame.mixer.Sound("./assets/explosionsfx.wav")  # <-- som da explosão
        self.explosion_sound.set_volume(0.4)

        # --- GRUPOS DE SPRITES ---
        self.player: Player = EntityFactory.get_entity('player')[0]
        self.player_group = pygame.sprite.GroupSingle(self.player)
        self.enemies = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()

        # spawn de inimigos
        self.enemy_spawn_timer = 0
        self.enemy_spawn_interval = 90  # frames (~1,5s a 60fps)

        # cooldown de tiro do player
        self.last_shot_time = 0
        self.shoot_cooldown = 300  # ms

    def run(self):
        pygame.mixer.music.load('./assets/levelsong.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        running = True
        while running:
            self.clock.tick(60)
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Atualizar backgrounds
            for bg in self.bg_layers:
                bg.update()

            # Movimento player
            self.player_group.update()

            # Tiro player
            current_time = pygame.time.get_ticks()
            if keys[pygame.K_SPACE] and current_time - self.last_shot_time > self.shoot_cooldown:
                bullet = Bullet("playershot", self.player.rect.midtop, direction=-1, speed=10)
                self.player_bullets.add(bullet)
                self.last_shot_time = current_time
                self.shoot_sound.play()

            # Spawn inimigos
            self.enemy_spawn_timer += 1
            if self.enemy_spawn_timer >= self.enemy_spawn_interval:
                self.enemy_spawn_timer = 0
                enemy_type = random.choice(['enemy1', 'enemy2', 'enemy3'])
                for enemy in EntityFactory.get_entity(enemy_type):
                    self.enemies.add(enemy)

            # Atualizar sprites
            self.enemies.update()
            self.player_bullets.update()
            self.enemy_bullets.update()
            self.explosions.update()

            # Inimigos tentam atirar
            for enemy in self.enemies:
                enemy.try_shoot(self.enemy_bullets)

            # Remoção de sprites fora da tela
            for enemy in list(self.enemies):
                if enemy.rect.top > HEIGHT:
                    self.enemies.remove(enemy)
            for bullet in list(self.player_bullets):
                if bullet.is_off_screen():
                    self.player_bullets.remove(bullet)
            for bullet in list(self.enemy_bullets):
                if bullet.is_off_screen():
                    self.enemy_bullets.remove(bullet)

            # Colisões
            hits = pygame.sprite.groupcollide(self.player_bullets, self.enemies, True, True)
            for bullet, enemies_hit in hits.items():
                for enemy in enemies_hit:
                    explosion = Explosion(enemy.rect.center, speed=3)
                    self.explosions.add(explosion)
                    self.explosion_sound.play()  # <-- toca som da explosão
                    print("Inimigo destruído!")

            if pygame.sprite.spritecollide(self.player_group.sprite, self.enemy_bullets, True):
                explosion = Explosion(self.player.rect.center, speed=3)
                self.explosions.add(explosion)
                self.explosion_sound.play()
                print("Player atingido!")

            if pygame.sprite.spritecollide(self.player_group.sprite, self.enemies, True):
                explosion = Explosion(self.player.rect.center, speed=3)
                self.explosions.add(explosion)
                self.explosion_sound.play()
                print("Player colidiu com inimigo!")

            # Desenho
            self.window.fill((0, 0, 0))
            for bg in self.bg_layers:
                self.window.blit(bg.image, bg.rect)

            self.player_group.draw(self.window)
            self.enemies.draw(self.window)
            self.player_bullets.draw(self.window)
            self.enemy_bullets.draw(self.window)
            self.explosions.draw(self.window)

            # debug info
            self.level_text(20, f'fps: {self.clock.get_fps():.0f}', WHITE, (10, HEIGHT - 35))
            self.level_text(20, f'inimigos: {len(self.enemies)}', WHITE, (10, HEIGHT - 20))
            self.level_text(20, f'tiros: {len(self.player_bullets) + len(self.enemy_bullets)}', WHITE, (10, HEIGHT - 50))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        font = pygame.font.Font("./assets/kenvector_future.ttf", text_size)
        surf = font.render(text, True, text_color).convert_alpha()
        rect = surf.get_rect(topleft=text_pos)
        self.window.blit(surf, rect)
