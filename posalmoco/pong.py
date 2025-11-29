import pygame 


pygame.init()
largura, altura = 500,500
janela  =  pygame.display.set_mode([largura, altura])
BRANCO = (255,255,255)
PRETO =  (0,0,0)

raquete1_x, raquete1_y = 40,225
raquete2_x, raquete2_y = 450,225
largura_raquete, altura_raquete  =  20,100
velocidade_raquete  =  1


bola_x, bola_y  = 250,250
velocidade_bola_x  = 0.1
velocidade_bola_y =  0.2
largura_bola, altura_bola =10,10

placar1 =  0
placar2 =  0

font  =  pygame.font.SysFont(None,20)


def desenhar():
    janela.fill(BRANCO)

    pygame.draw.rect(janela, PRETO,(raquete1_x, raquete1_y,largura_raquete, altura_raquete  )  )
    pygame.draw.rect(janela, PRETO,(raquete2_x, raquete2_y,largura_raquete, altura_raquete  )  )   
    pygame.draw.ellipse(janela, PRETO,(bola_x, bola_y ,largura_bola, altura_bola ) )
    placar_text = font.render(f'{placar1}    |    {placar2}', True, PRETO)
    # placar_text2 = font.render(f'{placar1}    |    {placar2}', True, PRETO)
    janela.blit(placar_text, (220,20))
    # janela.blit(placar_text2, (220,40))


run =  True
while run == True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
           run = False
           
    keys  =  pygame.key.get_pressed() 
    if keys[pygame.K_w] and raquete1_y > 0:
        raquete1_y -= velocidade_raquete
    if keys[pygame.K_s] and raquete1_y < 500 - altura_raquete:
        raquete1_y += velocidade_raquete    


    if keys[pygame.K_UP] and raquete2_y > 0:
        raquete2_y -= velocidade_raquete
    if keys[pygame.K_DOWN] and raquete2_y < 500 - altura_raquete:
        raquete2_y += velocidade_raquete  

    bola_x += velocidade_bola_x
    bola_y += velocidade_bola_y

# impede que ela saia da tela no eixo Y
    if bola_y <= 0 or bola_y >= 500 -altura_bola:
        velocidade_bola_y = - velocidade_bola_y

    if(raquete1_x < bola_x < raquete1_x + largura_raquete) and (raquete1_y < bola_y < raquete1_y + altura_raquete):
        velocidade_bola_x = - velocidade_bola_x
    if (raquete2_x < bola_x < raquete2_x + largura_raquete) and (raquete2_y < bola_y < raquete2_y + altura_raquete):
        velocidade_bola_x = - velocidade_bola_x

    if bola_x <=0:
        placar2   =  placar2 + 1
        bola_x, bola_y  = 200,90
   
        

    
    if bola_x >= 500:
        placar1   =  placar1 + 1
        bola_x, bola_y  = 200,90
   
    desenhar()
    pygame.display.update()

pygame.quit()















