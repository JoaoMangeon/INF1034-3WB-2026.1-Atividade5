from pygame import *
import sys

init()

rigbymordecai_img = image.load('rigbymordecai.png')
rigbymordecai_img = transform.scale(rigbymordecai_img, (225, 200))

rigbymordecai_font = font.Font('IceCreamParty.ttf', 50)

mixer.music.load


window = display.set_mode((1280,720))


window.fill((209, 245, 255))



while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit
    
    # Desenhar a partir daqui

    # Desenhar primitivas geométricas
    draw.rect(window, (159, 212, 101), (0, 600, 1280, 250))
    draw.rect(window, (168, 222, 202), (250, 350, 225, 250))
    draw.circle(window, (255, 247, 185), (120, 150), 60)
    draw.polygon(window, (118, 139, 126), ((300, 350), (400, 200), (500, 350)))
    
    # Desenhar imagens
    window.blit(rigbymordecai_img, (0, 0))

    # Desenhar texto
    rigbymordecai_text = rigbymordecai_font.render('REGULAR SHOW', True, (0,0,0))
    window.blit(rigbymordecai_text, (100, 430))
    
    display.update()