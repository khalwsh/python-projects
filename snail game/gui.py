import pygame
import time

from sys import exit

class SnailGame:
    """
    A class to represent a simple side-scrolling runner game where the player must avoid snails.
    """

    def __init__(self):
        """
        Initialize the game, including setting up the display, loading images, and defining game variables.
        """
        pygame.init()  # Initialize pygame

        frame_rate = 60
        screen = pygame.display.set_mode((800, 400))  # Create the main window

        sky_surface = pygame.image.load('graphics\\Sky.png').convert()  # Load the sky surface
        ground_surface = pygame.image.load('graphics\\ground.png').convert()  # Load the ground surface

        pygame.display.set_caption("Pixel Runner")  # Set the game caption

        Score_font = pygame.font.Font('font\\Pixeltype.ttf', 50)  # Create a pixel-style font for the score
        score = 0
        Score_Text = Score_font.render(f'Score = {score}', False, (64, 64, 64))  # Render the initial score text
        Score_rect = Score_Text.get_rect(center=(400, 50))  # Create a rectangle for the score text for easy positioning

        snail_surface = pygame.image.load('graphics\\snail\\snail2.png').convert_alpha()  # Load the snail image
        snail_rect = snail_surface.get_rect(bottomleft=(670, 300))  # Create a rectangle for the snail to position it easily
        clock = pygame.time.Clock()  # Create a clock to control the frame rate

        player_surface1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()  # Load player walk 1 image
        player_rect = player_surface1.get_rect(bottomleft=(60, 0))  # Create a rectangle for the player for easy positioning
        player_surface2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()  # Load player walk 2 image

        player_move = 0  # Counter for swapping between player walk 1 and 2 images to create the illusion of movement
        player_gravity = 0  # Variable to track player gravity for jumping and falling

        tim = time.time()  # Initialize a timer for score updates

        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Event to close the main screen
                    pygame.quit()
                    exit()  # Avoid runtime errors by exiting when the screen is closed

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if player_rect.bottom == 300:
                            player_gravity = -20  # Jump when the left mouse button is pressed and player is on the ground

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if player_rect.bottom >= 300:
                            player_gravity = -20  # Jump when the space key is pressed and player is on the ground

            if time.time() - tim >= 1:
                score += 1  # Update the score every second
                tim = time.time()
                
            Score_Text = Score_font.render(f'Score = {score}', False, (64, 64, 64))  # Render the updated score text
            screen.blit(sky_surface, (0, 0))  # Blit the sky surface onto the screen
            
            screen.blit(ground_surface, (0, 300))  # Blit the ground surface onto the screen
            
            pygame.draw.rect(screen, '#c0e8ec', Score_rect)  # Draw a rectangle around the score text
            pygame.draw.rect(screen, "#c0e8ec", Score_rect, 10)  # Draw the border of the rectangle around the score text
            screen.blit(Score_Text, Score_rect)  # Blit the score text onto the screen
            
            screen.blit(snail_surface, snail_rect)  # Blit the snail onto the screen

            # Player movement and gravity
            player_gravity += 1
            player_rect.bottom += player_gravity
            if player_rect.bottom >= 300:
                player_rect.bottom = 300

            # Alternate between player walk 1 and walk 2 images to create the walking animation
            if player_move < 10:
                screen.blit(player_surface1, player_rect)  # Walk 1
            else:
                screen.blit(player_surface2, player_rect)  # Walk 2

            player_move += 1  # Update the counter for player movement
            if player_move == 20:
                player_move = 0

            # Move the snail to the left
            snail_rect.left -= 5
            if snail_rect.left < -100:
                snail_rect.left = 800  # Reset snail position when it moves off screen

            # Check for collision between player and snail
            if player_rect.colliderect(snail_rect):
                
                while True:
                    done = False
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:  # Event to close the main screen
                            pygame.quit()
                            exit()  # Avoid runtime errors by exiting when the screen is closed
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                done = True  # Restart the game if space key is pressed
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if pygame.mouse.get_pressed()[0]:
                                done = True  # Restart the game if left mouse button is pressed

                    if done:
                        score = -1  # Reset the score
                        snail_rect.left = 800  # Reset the snail position
                        break

                    Score_font = pygame.font.Font('font\\Pixeltype.ttf', 50)  # Create a pixel-style font for game over text
                    Score_Text = Score_font.render('GAME OVER', False, (64, 64, 64))  # Render the game over text
                    Score_rect = Score_Text.get_rect(center=(400, 50))  # Create a rectangle for the game over text for easy positioning
                    
                    # give a restart option
                    restart_font = pygame.font.Font('font\\Pixeltype.ttf', 50)
                    restart_text = restart_font.render('Restart ?', False, (64, 64, 64))
                    restart_rect = restart_text.get_rect(center=(400, 80))
                    
                    screen.blit(sky_surface, (0, 0))  # Blit the sky surface onto the screen
                    
                    screen.blit(ground_surface, (0, 300))  # Blit the ground surface onto the screen
                    
                    pygame.draw.rect(screen, '#c0e8ec', Score_rect)  # Draw a rectangle around the game over text
                    pygame.draw.rect(screen, "#c0e8ec", Score_rect, 10)  # Draw the border of the rectangle around the game over text
                    screen.blit(Score_Text, Score_rect)  # Blit the game over text onto the screen
                    
                    pygame.draw.rect(screen, '#c0e8ec', restart_rect)  # Draw a rectangle around the restart text
                    pygame.draw.rect(screen, "#c0e8ec", restart_rect, 10)  # Draw the border of the rectangle around the restart text
                    screen.blit(restart_text, restart_rect)  # Blit the restart text onto the screen
                    
                    screen.blit(snail_surface, snail_rect)  # Blit the snail onto the screen
                    
                    pygame.display.update()  # Reload the next frame
                    clock.tick(frame_rate)  # Control the frame rate

            pygame.display.update()  # Reload the next frame
            clock.tick(frame_rate)  # Control the frame rate

    def __str__(self):
        """
        Return a string representation of the game state.
        """
        return f"SnailGame(score={self.score}, player_position={self.player_rect.topleft}, snail_position={self.snail_rect.topleft})"

    def __repr__(self):
        """
        Return an unambiguous string representation of the game state.
        """
        return self.__str__()

if __name__ == '__main__':
    app = SnailGame()
