import pygame
from network import Network
import player_file
from pygame import mixer
pygame.init()
width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tanks")
pygame.font.init()
background = pygame.image.load('background.png')
bulletImg = pygame.image.load('bullet.png')
# mixer.music.load('Power Bots Loop.wav')
# mixer.music.play(-1)
end_font = pygame.font.SysFont('arial', 64)


def redrawWindow(win, player1, player2):

    win.blit(background,(0,0))
    player1.draw(win)
    player2.rotate_and_draw(win)
    pygame.display.update()


def main():

    run = True
    n = Network()
    p = n.getP()
    player_file.tank1_image = pygame.transform.rotate(pygame.image.load('g.png'), 180)
    player_file.tank2_image = pygame.image.load('r.png')
    player_file.bullet_image = bulletImg
    clock = pygame.time.Clock()

    while run:

        clock.tick(14)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move(win, p2.x, p2.y, p2.dir_lurd)
        redrawWindow(win, p, p2)

        if p.opponents_hp == 0:

            p.end_game(win, 1, end_font)
            break

        if p2.opponents_hp == 0:

            p.end_game(win, 0, end_font)
            break

        if p2.bullet_state == "fire":

            p2.draw_bullet(win)

        if p.bullet_state == "fire":

            is_hit = p.fire_bullet(p.bulletX, p.bulletY, p.bullet_lurd, win, p2.x, p2.y, p2.dir_lurd)

            if is_hit == 'hit':

                p.minus_hp()

        pygame.display.update()


main()

