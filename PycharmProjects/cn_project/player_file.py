import pygame
import time
tank1_image = 'global image1'
tank2_image = 'global image2'
bullet_image = 'global bullet'


class Player():

    def __init__(self, x, y, tank_image_file, place, dir_lurd, hp):

        self.x = x
        self.y = y
        self.tank_velocity = 10
        self.bullet_velocity = 20
        self.dir_lurd = dir_lurd
        self.bullet_image_file = 'bullet.png'
        self.bulletX = 1000
        self.bulletY = 1000
        self.tank_image_file = tank_image_file
        self.place = place
        self.bullet_lurd = [0,0,0,0]
        self.bullet_state = "ready"
        self.angle = 0
        self.width = 500
        self.height = 500
        self.bullet_length = 0
        self.opponents_hp = hp

    def get_place(self):
        return self.place

    def minus_hp(self):
        self.opponents_hp = self.opponents_hp - 1

    def end_game(self, win, victory, end_font):
        pygame.font.init()
        if victory:
            text = end_font.render('YOU WIN!', True, (255, 255, 255))
        else:
            text = end_font.render('YOU LOSE!', True, (255, 255, 255))
        win.blit(text, (110, 200))
        pygame.display.update()
        time.sleep(4)

    def get_tank_image_file(self):
        return self.tank_image_file

    def draw(self, win):

        global tank1_image, tank2_image

        if self.place == 'top':
            tank_image = tank1_image
        else:
            tank_image = tank2_image

        win.blit(tank_image, (self.x, self.y))

    def rotate_and_draw(self, win):

        global tank1_image, tank2_image

        if self.place == 'top':
            tank1_image = pygame.transform.rotate(tank1_image, self.angle)
            win.blit(tank1_image, (self.x, self.y))
        else:
            tank2_image = pygame.transform.rotate(tank2_image, self.angle)
            win.blit(tank2_image, (self.x, self.y))

        self.angle = 0

    def draw_bullet(self, win):

        global bullet_image

        if self.bullet_lurd == [1, 0, 0, 0]:
            bull_rot_im = pygame.transform.rotate(bullet_image, 90)
            win.blit(bull_rot_im, (self.bulletX, self.bulletY + 5))

        if self.bullet_lurd == [0, 1, 0, 0]:
            bull_rot_im = bullet_image
            win.blit(bull_rot_im, (self.bulletX + 5, self.bulletY))

        if self.bullet_lurd == [0, 0, 1, 0]:
            bull_rot_im = pygame.transform.rotate(bullet_image, -90)
            win.blit(bull_rot_im, (self.bulletX + 45, self.bulletY + 5))

        if self.bullet_lurd == [0, 0, 0, 1]:
            bull_rot_im = pygame.transform.rotate(bullet_image, 180)
            win.blit(bull_rot_im, (self.bulletX + 6, self.bulletY + 50))

    def fire_bullet(self, bulletX, bulletY, lurd, win, x_aim, y_aim, lurd_aim):

        global bullet_image

        self.bulletX = bulletX
        self.bulletY = bulletY
        self.bullet_lurd = lurd
        self.bullet_state = "fire"
        self.bullet_length += self.bullet_velocity


        if (lurd == [0,1,0,0] or lurd == [0,0,0,1]) and (lurd_aim == [0,1,0,0] or lurd_aim == [0,0,0,1]) and\
                (x_aim-17<self.bulletX<x_aim+17) and (y_aim-55<self.bulletY<y_aim+65):
            self.bullet_state = 'ready'
            return 'hit'

        if (lurd == [1,0,0,0] or lurd == [0,0,1,0]) and (lurd_aim == [0,1,0,0] or lurd_aim == [0,0,0,1]) and\
                (x_aim-50<self.bulletX<x_aim+20) and (y_aim-5<self.bulletY<y_aim+50):
            self.bullet_state = 'ready'
            return 'hit'

        if (lurd == [0,1,0,0] or lurd == [0,0,0,1]) and (lurd_aim == [1,0,0,0] or lurd_aim == [0,0,1,0]) and\
                (x_aim -13<self.bulletX<x_aim+45) and (y_aim-65<self.bulletY<y_aim+30):
            self.bullet_state = 'ready'
            return 'hit'

        if (lurd == [1,0,0,0] or lurd == [0,0,1,0]) and (lurd_aim == [1,0,0,0] or lurd_aim == [0,0,1,0]) and\
                (x_aim-65<self.bulletX<x_aim+65) and (y_aim-17<self.bulletY<y_aim+17):
            self.bullet_state = 'ready'
            return 'hit'

        if self.bullet_lurd == [1, 0, 0, 0]:

            bull_rot_im = pygame.transform.rotate(bullet_image, 90)
            win.blit(bull_rot_im, (self.bulletX-20, self.bulletY+5))
            self.bulletX -= self.bullet_velocity

        if self.bullet_lurd == [0, 1, 0, 0]:

            bull_rot_im = bullet_image
            win.blit(bull_rot_im, (self.bulletX+5, self.bulletY-20))
            self.bulletY -= self.bullet_velocity

        if self.bullet_lurd == [0, 0, 1, 0]:

            bull_rot_im = pygame.transform.rotate(bullet_image, -90)
            win.blit(bull_rot_im, (self.bulletX+65, self.bulletY+5))
            self.bulletX += self.bullet_velocity

        if self.bullet_lurd == [0, 0, 0, 1]:

            bull_rot_im = pygame.transform.rotate(bullet_image, 180)
            win.blit(bull_rot_im, (self.bulletX+6, self.bulletY+70))
            self.bulletY += self.bullet_velocity

        if self.bullet_length >= 420:
            self.bullet_state = "ready"

        return 'not_hit'

    def rotate(self, old_lurd, new_lurd, win):

        global tank1_image, tank2_image
        dif = old_lurd.index(1) - new_lurd.index(1)
        self.angle = 90 * dif

        if self.place == 'top':
            tank1_image = pygame.transform.rotate(tank1_image, self.angle)
            win.blit(tank1_image, (self.x, self.y))
        else:
            tank2_image = pygame.transform.rotate(tank2_image, self.angle)
            win.blit(tank2_image, (self.x, self.y))

        pygame.display.flip()

    def move(self, win, second_x, second_y, second_lurd):
        self.angle = 0
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_LEFT] and (keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]))\
                or (keys[pygame.K_UP] and keys[pygame.K_DOWN]) or (keys[pygame.K_RIGHT] and (keys[pygame.K_DOWN] or keys[pygame.K_UP])):
            return

        if keys[pygame.K_SPACE]:
            if self.bullet_state == "ready":
                self.bullet_length = 0
                # self.fire_bullet(self.x, self.y, self.dir_lurd, win)
                self.bulletX = self.x
                self.bulletY = self.y
                self.bullet_lurd = self.dir_lurd
                self.bullet_state = "fire"

        if keys[pygame.K_LEFT]:

            new_lurd = [1,0,0,0]
            self.rotate(self.dir_lurd,new_lurd, win)
            self.dir_lurd = new_lurd

            if self.x <= 0:
                self.x = 0
            else:
                new_x = self.x - self.tank_velocity
                if second_lurd == [0,1,0,0]:
                    if ((second_x -5 < new_x < second_x + 14) and (second_y - 25 < self.y < second_y + 45)):
                        return
                if second_lurd == [0,0,0,1]:
                    if ((second_x - 5 < new_x < second_x + 14) and (second_y - 30 < self.y < second_y + 50)):
                        return
                if second_lurd == [0,0,1,0]:
                    if ((second_x +20 < new_x < second_x + 35) and (second_y - 25 < self.y < second_y + 32)):
                        return
                if second_lurd == [1,0,0,0]:
                    if ((second_x +35 < new_x < second_x + 50) and (second_y - 15 < self.y < second_y + 50)):
                        return
                self.x = new_x
            return

        if keys[pygame.K_RIGHT]:

            new_lurd = [0, 0, 1, 0]
            self.rotate(self.dir_lurd, new_lurd, win)
            self.dir_lurd = new_lurd

            if self.x >= 430:
                self.x = 430
            else:
                new_x = self.x + self.tank_velocity
                if second_lurd == [0,1,0,0]:
                    if ((second_x - 52 < new_x < second_x-32) and (second_y - 20 < self.y < second_y + 70)):
                        return
                if second_lurd == [0,0,0,1]:
                    if ((second_x - 55 < new_x < second_x-35) and (second_y - 30 < self.y < second_y + 50)):
                        return
                if second_lurd == [0,0,1,0]:
                    if ((second_x - 55 < new_x < second_x-40) and (second_y - 30 < self.y < second_y + 24)):
                        return
                if second_lurd == [1,0,0,0]:
                    if ((second_x - 25 < new_x < second_x-10) and (second_y - 30 < self.y < second_y + 30)):
                        return

                self.x = new_x
            return

        if keys[pygame.K_UP]:

            new_lurd = [0, 1, 0, 0]
            self.rotate(self.dir_lurd, new_lurd, win)
            self.dir_lurd = new_lurd

            if self.y <= 0:
                self.y = 0
            else:
                new_y = self.y - self.tank_velocity
                if second_lurd == [0,1,0,0]:
                    if ((second_x - 30 < self.x < second_x + 30) and (second_y + 30 < new_y < second_y + 50)):
                        return
                if second_lurd == [0,0,0,1]:
                    if ((second_x - 30 < self.x < second_x + 30) and (second_y + 10 < new_y < second_y + 30)):
                        return
                if second_lurd == [0,0,1,0]:
                    if ((second_x - 30 < self.x < second_x + 50) and (second_y - 10 < new_y < second_y + 5)):
                        return
                if second_lurd == [1,0,0,0]:
                    if ((second_x - 20 < self.x < second_x + 70) and (second_y - 10 < new_y < second_y + 5)):
                        return
                self.y = new_y
            return

        if keys[pygame.K_DOWN]:

            new_lurd = [0, 0, 0, 1]
            self.rotate(self.dir_lurd, new_lurd, win)
            self.dir_lurd = new_lurd

            if self.y >= 430:
                self.y = 430
            else:
                new_y = self.y + self.tank_velocity
                if second_lurd == [0,1,0,0]:
                    if ((second_x - 30 < self.x < second_x + 30) and (second_y - 35 < new_y < second_y -15)):
                        return
                if second_lurd == [0,0,0,1]:
                    if ((second_x - 30 < self.x < second_x + 30) and (second_y - 45 < new_y < second_y-30 )):
                        return
                if second_lurd == [0,0,1,0]:
                    if ((second_x - 30 < self.x < second_x + 55) and (second_y - 45 < new_y < second_y-30 )):
                        return
                if second_lurd == [1,0,0,0]:
                    if ((second_x - 15 < self.x < second_x + 70) and (second_y - 45 < new_y < second_y-30 )):
                        return

                self.y = new_y
            return



