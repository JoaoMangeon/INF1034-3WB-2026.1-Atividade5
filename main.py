from pygame import *
import sys

init()

rigbymordecai_img = image.load('rigbymordecai.png')
rigbymordecai_img = transform.scale(rigbymordecai_img, (225, 200))

rigbymordecai_font = font.Font('IceCreamPartySolid.ttf', 50)

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
    draw.rect(window, (159, 212, 101), (0, 600, 1280, 350))
    draw.rect(window, (168, 222, 202), (350, 350, 235, 250))
    draw.circle(window, (255, 247, 185), (140, 100), 55)
    
    draw.polygon(window, (118, 139, 126), ((350, 350), (468, 150), (585, 350)))

    draw.rect(window, (170, 131, 140), (830, 450, 40, 150)) 
    draw.circle(window, (156, 204, 86), (850, 400), 100) 
    
    draw.circle(window, (255, 255, 255), (850, 100), 50)
    draw.circle(window, (255, 255, 255), (900, 100), 60)
    draw.circle(window, (255, 255, 255), (950, 100), 55)
    draw.circle(window, (255, 255, 255), (1000, 100), 50)

    draw.rect(window, (168, 222, 202), (350, 350, 235, 250))
    draw.rect(window, (168, 222, 202), (350, 350, 235, 250))
    draw.rect(window, (168, 222, 202), (350, 350, 235, 250))
    draw.rect(window, (168, 222, 202), (350, 350, 235, 250))
    draw.rect(window, (168, 222, 202), (350, 350, 235, 250))
    draw.rect(window, (168, 222, 202), (350, 350, 235, 250))
    draw.rect(window, (168, 222, 202), (350, 350, 235, 250))
    draw.rect(window, (168, 222, 202), (350, 350, 235, 250))
    

    
    # Desenhar imagens
    window.blit(rigbymordecai_img, (0, 410))

    # Desenhar texto
    rigbymordecai_text = rigbymordecai_font.render('REGULAR SHOW', True, (0,0,0))
    window.blit(rigbymordecai_text, (500, 0))
    
    display.update()