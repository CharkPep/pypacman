import pygame

resolution = (800, 800)

pygame.init()
screen = pygame.display.set_mode(resolution)
rect = pygame.rect.Rect((100, 100), (400, 400))
print(rect)
pygame.display.set_caption("Test")
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, (0, 0, 0), rect)

    if rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
        pygame.draw.rect(screen, (255, 0, 0), rect)

    pygame.display.flip()
    clock.tick(60)
