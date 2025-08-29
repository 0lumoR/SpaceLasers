import pygame
import random
from code.Const import WHITE, HEIGHT, WIDTH
from code.EntityFactory import EntityFactory
from code.Bullet import Bullet
from code.GameOver import GameOver
from code.Life import Life
from code.Player import Player
from code.Explosion import Explosion


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.bg_layers = EntityFactory.get_backgrounds()
        self.clock = pygame.time.Clock()

        # --- GRUPOS DE SPRITES ---
        self.player: Player = EntityFactory.get_entity('player')[0]
        self.player.health = 3
        self.player_group = pygame.sprite.GroupSingle(self.player)
        self.enemies = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.life_drops = pygame.sprite.Group()

        # HUD
        self.score = 0

        # spawn de inimigos
        self.enemy_spawn_timer = 0
        self.enemy_spawn_interval = 90  # frames

        # cooldown de tiro do player
        self.last_shot_time = 0
        self.shoot_cooldown = 300

        # timer
        self.start_time = pygame.time.get_ticks()
        self.elapsed_time = 0

        # sons
        pygame.mixer.init()
        self.shoot_sound = pygame.mixer.Sound("./assets/lasersfx.ogg")
        self.explosion_sound = pygame.mixer.Sound("./assets/explosionsfx.wav")

    def run(self):
        pygame.mixer.music.load('./assets/levelsong.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        while True:
            self.clock.tick(60)
            keys = pygame.key.get_pressed()

            # atualizar timer
            self.elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000

            # --- EVENTOS ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # --- ATUALIZAR BACKGROUNDS ---
            for bg in self.bg_layers:
                bg.update()

            # --- MOVIMENTO PLAYER ---
            self.player_group.update()

            # --- TIRO PLAYER ---
            if self.player_group:
                player = self.player_group.sprite
                current_time = pygame.time.get_ticks()
                if keys[pygame.K_SPACE] and current_time - self.last_shot_time > self.shoot_cooldown:
                    bullet = Bullet("playershot", player.rect.midtop, direction=-1, speed=10)
                    self.player_bullets.add(bullet)
                    self.shoot_sound.play()
                    self.last_shot_time = current_time

            # --- SPAWN DE INIMIGOS ---
            self.enemy_spawn_timer += 1
            if self.enemy_spawn_timer >= self.enemy_spawn_interval:
                self.enemy_spawn_timer = 0
                enemy_type = random.choice(['enemy1', 'enemy2', 'enemy3'])
                for enemy in EntityFactory.get_entity(enemy_type):
                    self.enemies.add(enemy)

            # --- MOVIMENTOS ---
            self.enemies.update()
            self.player_bullets.update()
            self.enemy_bullets.update()
            self.explosions.update()
            self.life_drops.update()

            # inimigos tentam atirar
            for enemy in self.enemies:
                enemy.try_shoot(self.enemy_bullets)

            # --- REMOÇÃO DE SPRITES FORA DA TELA ---
            for enemy in list(self.enemies):
                if enemy.rect.top > HEIGHT:
                    self.enemies.remove(enemy)
            for bullet in list(self.player_bullets):
                if bullet.is_off_screen():
                    self.player_bullets.remove(bullet)
            for bullet in list(self.enemy_bullets):
                if bullet.is_off_screen():
                    self.enemy_bullets.remove(bullet)

            # --- COLISÕES ---
            hits = pygame.sprite.groupcollide(self.player_bullets, self.enemies, True, True)
            for bullet, enemies_hit in hits.items():
                for enemy in enemies_hit:
                    self.score += 100
                    explosion = Explosion(enemy.rect.center, speed=2)
                    self.explosions.add(explosion)
                    self.explosion_sound.play()

                    # chance de dropar vida (ex: 20%)
                    if random.random() < 0.2:
                        life = Life(enemy.rect.center)
                        self.life_drops.add(life)

            if self.player_group:
                player = self.player_group.sprite

                # colisão com tiros inimigos
                if pygame.sprite.spritecollide(player, self.enemy_bullets, True):
                    player.health -= 1
                    if player.health <= 0:
                        explosion = Explosion(player.rect.center, speed=2)
                        self.explosions.add(explosion)
                        self.explosion_sound.play()
                        self.player_group.empty()
                        return GameOver(self.window, self.score).run()

                # colisão com inimigos
                if pygame.sprite.spritecollide(player, self.enemies, True):
                    player.health -= 1
                    if player.health <= 0:
                        explosion = Explosion(player.rect.center, speed=2)
                        self.explosions.add(explosion)
                        self.explosion_sound.play()
                        self.player_group.empty()
                        return GameOver(self.window, self.score).run()

                # colisão com drop de vida
                if pygame.sprite.spritecollide(player, self.life_drops, True):
                    player.health = min(player.health + 1, 3)

            # --- DESENHO ---
            for bg in self.bg_layers:
                self.window.blit(bg.image, bg.rect)

            self.player_group.draw(self.window)
            self.enemies.draw(self.window)
            self.player_bullets.draw(self.window)
            self.enemy_bullets.draw(self.window)
            self.explosions.draw(self.window)
            self.life_drops.draw(self.window)

            # HUD
            life_value = self.player_group.sprite.health if self.player_group else 0
            self.level_text(25, f'Life: {life_value}', (255, 50, 50), (10, 10))
            self.level_text(25, f'Score: {self.score}', (255, 255, 0), (WIDTH - 200, 10))
            minutes = self.elapsed_time // 60
            seconds = self.elapsed_time % 60
            self.level_text(25, f'Time: {minutes:02}:{seconds:02}', WHITE, (WIDTH//2 - 50, 10))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        font = pygame.font.Font("./assets/kenvector_future.ttf", text_size)
        surf = font.render(text, True, text_color).convert_alpha()
        rect = surf.get_rect(topleft=text_pos)
        self.window.blit(surf, rect)


