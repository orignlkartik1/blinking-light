import pygame

pygame.init()

color="red"
position=(0,0)


cav=pygame.display.set_mode((500,500),pygame.RESIZABLE)
pygame.display.set_caption("My pygame")


img=pygame.image.load(r'C:\Users\karti\OneDrive\Pictures\profile.png')
pygame.display.set_icon(img)
exit=False

while not exit:
    #cav.blit(img,position)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit=True

    cav.fill(color)
    pygame.display.flip()


    if color=="red":
        color="green"
    elif color=="green":
        color="blue"
    else:
        color="red"


