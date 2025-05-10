import pygame
import pygame_menu
import main as game
from enums.algorithm import Algorithm
import os

# --- Config ---
MENU_BACKGROUND_IMAGE = "background/background_bomberman.PNG"
MENU_FONT = pygame_menu.font.FONT_BEBAS
BUTTON_COLOR = (255, 255, 255)
SELECTION_COLOR = (200, 200, 200)

COLOR_BACKGROUND = (153, 153, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (102, 102, 153)
MENU_TITLE_COLOR = (51, 51, 255)
WINDOW_SCALE = 0.75

pygame.init()
INFO = pygame.display.Info()
TILE_SIZE = max(15, int(INFO.current_h * 0.035))  # Added safety floor
WINDOW_SIZE = (13 * TILE_SIZE, 13 * TILE_SIZE)

clock = pygame.time.Clock()
player_alg = Algorithm.PLAYER
en1_alg = Algorithm.DIJKSTRA
en2_alg = Algorithm.DFS
en3_alg = Algorithm.DIJKSTRA
show_path = True
surface = pygame.display.set_mode(WINDOW_SIZE)


def run_game():
    game.start_bomberman(surface, show_path, player_alg, en1_alg, en2_alg, en3_alg, TILE_SIZE)


def main_background():
    if os.path.exists(MENU_BACKGROUND_IMAGE):
        background_image = pygame_menu.BaseImage(
            image_path=MENU_BACKGROUND_IMAGE,
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
        )
    else:
        print(f"Warning: Background image not found: {MENU_BACKGROUND_IMAGE}")
        background_image = MENU_BACKGROUND_COLOR


def menu_loop():
    pygame.display.set_caption('Bomberman')

    # --- Load Background Image or Use Fallback ---
    if os.path.exists(MENU_BACKGROUND_IMAGE):
        background_image = pygame_menu.BaseImage(
            image_path=MENU_BACKGROUND_IMAGE,
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
        )
    else:
        print(f"Warning: Background image not found: {MENU_BACKGROUND_IMAGE}")
        background_image = MENU_BACKGROUND_COLOR  # fallback

    # --- Theme ---
    menu_theme = pygame_menu.Theme(
        background_color=background_image,
        selection_color=SELECTION_COLOR,
        widget_font=MENU_FONT,
        title_font_size=TILE_SIZE,
        title_font_color=COLOR_BLACK,
        title_font=MENU_FONT,
        widget_font_color=COLOR_BLACK,
        widget_font_size=int(TILE_SIZE * 0.7),
        title_background_color=MENU_TITLE_COLOR,
        widget_padding=10,
        widget_selection_effect=pygame_menu.widgets.HighlightSelection(),
        widget_alignment=pygame_menu.locals.ALIGN_CENTER,  # Add this to center all widgets
        title_offset=(0, 0),  # Adjust title vertical position if needed
        title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY  # Cleaner title bar
    )

    # --- Menus ---
    main_menu = pygame_menu.Menu(
        title='Main menu',
        width=13 * TILE_SIZE,
        height=13 * TILE_SIZE,
        theme=menu_theme,

    )

    play_menu = pygame_menu.Menu(
        theme=menu_theme,
        width=13 * TILE_SIZE,
        height=13 * TILE_SIZE,
        title='Play menu'
    )
    play_menu.add.button('Start', run_game, font_color=COLOR_BLACK, background_color=BUTTON_COLOR)
    play_menu.add.button('Return  to  main  menu', pygame_menu.events.BACK,
                         font_color=COLOR_BLACK, background_color=BUTTON_COLOR)

    keybinds_menu_theme = menu_theme.copy()
    keybinds_menu_theme.widget_font_size = int(TILE_SIZE * 0.5)

    keybinds_menu = pygame_menu.Menu(
        theme=keybinds_menu_theme,
        width=13 * TILE_SIZE,
        height=13 * TILE_SIZE,
        overflow=False,
        title='Keybinds'
    )
    keybinds_menu.add.label("Player 1 Controls:", font_color=COLOR_BLACK)
    keybinds_menu.add.label("Move: Q, Z, D, S", font_color=COLOR_BLACK)
    keybinds_menu.add.label("Plant Bomb: E", font_color=COLOR_BLACK)
    keybinds_menu.add.vertical_margin(0.5)
    keybinds_menu.add.label("Player 2 Controls:", font_color=COLOR_BLACK)
    keybinds_menu.add.label("Move: Arrow Keys", font_color=COLOR_BLACK)
    keybinds_menu.add.label("Plant Bomb: Shift", font_color=COLOR_BLACK)
    keybinds_menu.add.vertical_margin(0.5)
    keybinds_menu.add.button('Return  to  main  menu', pygame_menu.events.BACK,
                             font_color=COLOR_BLACK, background_color=BUTTON_COLOR)

    special_attack_menu_theme = menu_theme.copy()
    special_attack_menu_theme.widget_font_size = int(TILE_SIZE * 0.5)

    special_attack_menu = pygame_menu.Menu(
        theme=special_attack_menu_theme,
        width=13 * TILE_SIZE,
        height=13 * TILE_SIZE,
        overflow=False,
        title='Special Attack'
    )
    special_attack_menu.add.label("Each player gains a special ", font_color=COLOR_BLACK)
    special_attack_menu.add.label("attack after destroying 5 ", font_color=COLOR_BLACK)
    special_attack_menu.add.label("blocks.", font_color=COLOR_BLACK)
    special_attack_menu.add.vertical_margin(5)
    special_attack_menu.add.label("Use the same movement ", font_color=COLOR_BLACK)
    special_attack_menu.add.label("keys to aim.  Player ", font_color=COLOR_BLACK)
    special_attack_menu.add.label("remains stationary during ", font_color=COLOR_BLACK)
    special_attack_menu.add.label("special attack.", font_color=COLOR_BLACK)
    special_attack_menu.add.vertical_margin(5)
    special_attack_menu.add.button('Return  to  main  menu', pygame_menu.events.BACK,
                                   font_color=COLOR_BLACK, background_color=BUTTON_COLOR)

    # --- Main Menu Buttons ---
    main_menu.add.button('Play', play_menu, font_color=COLOR_BLACK, background_color=BUTTON_COLOR)
    main_menu.add.button('Keybinds', keybinds_menu, font_color=COLOR_BLACK, background_color=BUTTON_COLOR)
    main_menu.add.button('Special Attack', special_attack_menu, font_color=COLOR_BLACK,
                         background_color=BUTTON_COLOR)
    main_menu.add.button('Quit', pygame_menu.events.EXIT, font_color=COLOR_BLACK, background_color=BUTTON_COLOR)

    if MENU_BACKGROUND_IMAGE and os.path.exists(MENU_BACKGROUND_IMAGE):
        try:
            main_menu.bg_color = pygame_menu.baseimage.BaseImage(
                image_path=MENU_BACKGROUND_IMAGE,
                drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
            )
        except pygame.error as e:
            print(f"Error setting background image: {e}")
            main_menu.bg_color = MENU_BACKGROUND_COLOR
    else:
        main_menu.bg_color = MENU_BACKGROUND_COLOR

    running = True
    while running:
        clock.tick(FPS)
        main_background()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        if main_menu.is_enabled():
            main_menu.mainloop(surface, main_background)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    menu_loop()
