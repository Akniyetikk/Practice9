import pygame
import sys
from player import MusicPlayer


WIDTH, HEIGHT = 640, 480
FPS = 30


COLOR_BG = (20, 20, 30)
COLOR_TEXT = (255, 255, 255)
COLOR_ACCENT = (0, 255, 150)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Music Player")
    clock = pygame.time.Clock()
    

    player = MusicPlayer(music_folder="music")
    font = pygame.font.SysFont("Arial", 24)
    font_small = pygame.font.SysFont("Arial", 18)

    running = True
    while running:
        screen.fill(COLOR_BG)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: player.play()
                if event.key == pygame.K_s: player.stop()
                if event.key == pygame.K_SPACE: player.pause_resume()
                if event.key == pygame.K_n: player.next_track()
                if event.key == pygame.K_b: player.prev_track()
                if event.key == pygame.K_q: running = False

        player.update()


        track_text = font.render(f"Трек: {player.get_track_name()}", True, COLOR_TEXT)
        status_text = font.render(f"Статус: {player.get_status()}", True, COLOR_ACCENT)
        time_text = font_small.render(f"Время: {player.get_position_seconds()} сек.", True, COLOR_TEXT)
        
        screen.blit(track_text, (50, 100))
        screen.blit(status_text, (50, 150))
        screen.blit(time_text, (50, 200))

    
        controls = "P: Play | S: Stop | Space: Pause | N: Next | B: Back | Q: Quit"
        controls_surf = font_small.render(controls, True, (150, 150, 150))
        screen.blit(controls_surf, (50, 400))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
