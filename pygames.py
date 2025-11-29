# import pygame
# import sys

# pygame.init()

# width = 700
# height = 500

# screen = pygame.display.set_mode((width, height)) 

# quandrado =  pygame.Rect(350,200, 150,70)
# rectangulo2 = pygame.Rect(10,150, 50,50)

# clock =  pygame.time.Clock()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#            pygame.quit() 
#            sys.exit()
        
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 quandrado.move_ip([10,0])
#             if event.key == pygame.K_LEFT:
#                 quandrado.move_ip([-10,0])
#             if event.key == pygame.K_UP:
#                 quandrado.move_ip([0,-10])
#             if event.key == pygame.K_DOWN:
#                 quandrado.move_ip([0,10])     

        
#         screen.fill('red')
#         pygame.draw.rect(screen,('green'), quandrado)
#         pygame.draw.rect(screen,('white'), rectangulo2)
#         pygame.display.update()








import pygame 
import sys

pygame.init()

tela =  pygame.display.set_mode([500,500])
# run = True

quadrado   =  pygame.Rect(15,20,10,10)


clock =  pygame.time.Clock()

while True:
      for eventos in pygame.event.get():
          if eventos.type  == pygame.QUIT:
            #    run = False 
               pygame.quit()
               sys.exit()       
      
          if eventos.type == pygame.KEYDOWN:
               if eventos.key  == pygame.K_RIGHT:
                  quadrado.move_ip([10,0])
               if eventos.key == pygame.K_LEFT:
                    quadrado.move_ip([-10,0])  

               if eventos.key == pygame.K_UP:
                    quadrado.move_ip([0,-10])

               if eventos.key == pygame.K_DOWN:
                    quadrado.move_ip([0,10])            
          tela.fill('red')
          pygame.draw.rect(tela, 'green', quadrado)
      

   
          pygame.display.update()   

     