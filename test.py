import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Schrodinger's Cat")


#main game loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()

        

clock = pygame.time.Clock()








pygame.quit()
quit()
