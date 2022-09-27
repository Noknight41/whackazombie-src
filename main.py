import pygame
import random
from pygame import *


class GameManager:
    # Initialize startup
    def __init__(self):
        # Initialize screen
        pygame.display.set_caption("Whack A Zombie")
        self.screen = pygame.display.set_mode((1080, 600))
        self.font = pygame.font.Font('images/PIXEL.ttf', 31)
        self.sound = SoundEffect()
        # Initialize holes
        self.hole = []
        self.hole.append((130, 97))
        self.hole.append((302, 97))
        self.hole.append((464, 97))
        self.hole.append((650, 97))
        self.hole.append((825, 97))
        self.hole.append((157, 250))
        self.hole.append((310, 250))
        self.hole.append((486, 250))
        self.hole.append((674, 250))
        self.hole.append((858, 250))
        self.hole.append((300, 432))
        self.hole.append((527, 432))
        self.hole.append((754, 432))
        # Initialize zombie animation sheet
        animation = pygame.image.load("images/zombie.png")
        self.zom = []
        col1 = []
        col1.append(animation.subsurface(17, 90, 113, 91))
        col1.append(animation.subsurface(170, 90, 113, 91))
        col1.append(animation.subsurface(347, 90, 113, 91))
        col1.append(animation.subsurface(529, 90, 113, 91))
        col1.append(animation.subsurface(700, 90, 113, 91))
        col1.append(animation.subsurface(878, 90, 113, 91))
        col2 = []
        col2.append(animation.subsurface(17, 260, 113, 91))
        col2.append(animation.subsurface(170, 260, 113, 91))
        col2.append(animation.subsurface(347, 260, 113, 91))
        col2.append(animation.subsurface(529, 260, 113, 91))
        col2.append(animation.subsurface(700, 260, 113, 91))
        col2.append(animation.subsurface(878, 260, 113, 91))
        col3 = []
        col3.append(animation.subsurface(17, 440, 113, 91))
        col3.append(animation.subsurface(170, 440, 113, 91))
        col3.append(animation.subsurface(347, 440, 113, 91))
        col3.append(animation.subsurface(529, 440, 113, 91))
        col3.append(animation.subsurface(700, 440, 113, 91))
        col3.append(animation.subsurface(878, 440, 113, 91))
        self.zom.append(col1)
        self.zom.append(col2)
        self.zom.append(col3)

    # Check if button is hit
    def hit(self, mouse, pos, w, h):
        x = mouse[0]
        y = mouse[1]
        x2 = pos[0]
        y2 = pos[1]
        if (x > x2) and (x < x2 + w) and (y > y2) and (y < y2 + h):
            return True
        else:
            return False

    # Update statistic
    def update(self):
        # Back button
        score_text = self.font.render("BACK", True, (255, 255, 255))
        score_pos = score_text.get_rect()
        score_pos.centerx = 80
        score_pos.centery = 550
        self.screen.blit(score_text, score_pos)
        # Update score/misses ratio
        score_text = self.font.render("HITS/MISSES: " + str(self.score) + "/" + str(self.misses), True, (255, 255, 255))
        score_pos = score_text.get_rect()
        score_pos.centerx = 216
        score_pos.centery = 25
        self.screen.blit(score_text, score_pos)
        # Update level
        if self.level == 1:
            level_string = "LEVEL: EASY"
            self.interval = 0.8
        elif self.level == 2:
            level_string = "LEVEL: NORMAL"
            self.interval = 0.6
        elif self.level == 3:
            level_string = "LEVEL: HARD"
            self.interval = 0.45
        elif self.level == 4:
            level_string = "LEVEL: INSANE"
            self.interval = 0.3
        else:
            level_string = "LEVEL: GODLIKE"
            self.interval = 0.15
        level_text = self.font.render(level_string, True, (255, 255, 255))
        level_pos = level_text.get_rect()
        level_pos.centerx = 864
        level_pos.centery = 25
        self.screen.blit(level_text, level_pos)

    # Win screen
    def win(self):
        win_text = self.font.render("YOU WIN", True, (255, 255, 255))
        win_pos = win_text.get_rect()
        win_pos.centerx = self.bg.get_rect().centerx
        win_pos.centery = self.bg.get_rect().centery
        self.screen.blit(win_text, win_pos)
        pygame.display.flip()
        clock = 0
        while True:
            clock += pygame.time.Clock().tick(60) / 1000
            if clock > 3:
                return
    
    # Lose screen
    def lose(self):
        lose_text = self.font.render("YOU LOSE, YOUR HIGHSCORE: " + str(self.score), True, (255, 255, 255))
        lose_pos = lose_text.get_rect()
        lose_pos.centerx = self.bg.get_rect().centerx
        lose_pos.centery = self.bg.get_rect().centery
        self.screen.blit(lose_text, lose_pos)
        pygame.display.flip()
        clock = 0
        while True:
            clock += pygame.time.Clock().tick(60) / 1000
            if clock > 3:
                return
        
    # Game loop
    def start(self):
        # Initialize statistic
        pygame.display.flip()
        self.level = 1
        self.score = 0
        self.misses = 0
        self.interval = 1
        # Define variables
        self.bg = pygame.image.load("images/bg.jpg")
        pygame.mixer.music.load("sounds/gameplay.wav")
        mixer.music.play(-1)
        mixer.music.set_volume(0.18)
        clock = 0
        state = -1
        loop = True
        live = False
        interval = 0
        grave = 0
        skin = 0

        while loop:
            # Lose condition
            if self.misses == 5:
                loop = False
                self.lose()
                self.menu()
            # Win condition
            if self.level == 6:
                loop = False
                self.win()
                self.menu()
            for event in pygame.event.get():
                # Allow exit
                if event.type == pygame.QUIT:
                    loop = False
                # Mouse click
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    self.sound.playClick()
                    # Back to menu
                    if self.hit(mouse.get_pos(), [50,520], 62, 62):
                        loop = False
                        self.menu()
                    # Hit zombie
                    if self.hit(mouse.get_pos(), self.hole[grave], 113, 91) and state < 4:
                        state = 3                       
                        live = False
                        interval = 0
                        self.score += 1 
                        self.level = 1 + int(self.score / 5)
                        if (self.score % 5) == 0:
                            self.sound.playLevel()
                        self.sound.playHit()
                    else:
                        self.misses += 1
                    self.update()

            # Delete killed zombie
            if state > 5:
                self.screen.blit(self.bg, (0, 0))
                self.update()
                state = -1
                
            # Random a new zombie
            if state == -1:
                self.screen.blit(self.bg, (0, 0))
                self.update()
                self.sound.playPop()
                state = 0
                live = False
                interval = 0.3
                grave = random.randint(0, 12)
                skin = random.randint(0, 2)

            # Animation timing
            clock += pygame.time.Clock().tick(60) / 1000
            if clock > interval:
                self.screen.blit(self.bg, (0, 0))
                self.screen.blit(self.zom[skin][state], (self.hole[grave][0], self.hole[grave][1]))
                self.update()
                if live is True:
                    state -= 1
                else:
                    state += 1
                if state == 3:
                    state -= 1
                    live = True            
                    interval = self.interval
                else:
                    interval = 0.1
                clock = 0
            # Update the display
            pygame.display.flip()

    # Credit loop
    def credit(self):
        # Define variables:
        credit = pygame.image.load("images/credit.png")
        loop = True
        while loop:
            for event in pygame.event.get():
                # Allow exit
                if event.type == pygame.QUIT:
                    loop = False
                # Mouse click
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    self.sound.playClick()
                    # Back to menu
                    if self.hit(mouse.get_pos(), [473,410], 160, 33):
                        loop = False
                        return
            self.screen.blit(credit, (0, 0))
            pygame.display.flip()

    # Menu loop
    def menu(self):
        # Define variables:
        pygame.display.flip()
        self.bg = pygame.image.load("images/menu.png")
        pygame.mixer.music.load("sounds/menu.wav")
        mixer.music.play(-1)
        mixer.music.set_volume(0.18)
        loop = True

        while loop:
            for event in pygame.event.get():
                # Allow exit
                if event.type == pygame.QUIT:
                    loop = False
                # Mouse click
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    self.sound.playClick()
                    # Play game
                    if self.hit(mouse.get_pos(), [587,145], 321, 98):
                        loop = False
                        self.start()
                    # Show credit
                    if self.hit(mouse.get_pos(), [600,311], 268, 86):         
                        self.credit()

            # Update the display
            self.screen.blit(self.bg, (0, 0))
            pygame.display.flip()
####
# Initialize sound
class SoundEffect:
    def __init__(self):
        self.clickSound = pygame.mixer.Sound("sounds/click.wav")
        self.popSound = pygame.mixer.Sound("sounds/pop.wav")
        self.hitSound = pygame.mixer.Sound("sounds/hit.wav")
        self.levelSound = pygame.mixer.Sound("sounds/level.wav")
        self.clickSound.set_volume(0.08)
        self.popSound.set_volume(0.08)
        self.hitSound.set_volume(0.15)
        self.levelSound.set_volume(0.08)

    def playClick(self):
        self.clickSound.play()

    def playPop(self):
        self.popSound.play()

    def playHit(self):
        self.hitSound.play()

    def playLevel(self):
        self.levelSound.play()

#####
# Initialize game
pygame.init()
game = GameManager()
game.menu()
pygame.quit()
