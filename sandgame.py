import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sand Incremental Game")

# Set up game variables
sand_count = 0
sand_per_click = 1
sand_increment_cost = 10

font = pygame.font.Font(None, 36)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                sand_count += sand_per_click
            elif event.button == 3:  # Right mouse button
                if sand_count >= sand_increment_cost:
                    sand_count -= sand_increment_cost
                    sand_per_click += 1
                    sand_increment_cost *= 2

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw sand count
    text = font.render(f"Sand: {sand_count}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Draw sand per click and cost
    text = font.render(f"Sand per click: {sand_per_click}", True, (0, 0, 0))
    screen.blit(text, (10, 50))
    text = font.render(f"Upgrade Cost: {sand_increment_cost}", True, (0, 0, 0))
    screen.blit(text, (10, 90))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
