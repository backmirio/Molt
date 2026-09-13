import pygame as pg

from random import randrange

pg.init()

WINDOW = 1000
TILE_SIZE = 50

GAME_MIN = 100 + TILE_SIZE // 2
GAME_MAX = 900 - TILE_SIZE // 2

GRID_SIZE = 16
MAX_LENGTH = GRID_SIZE * GRID_SIZE

RANGE = (GAME_MIN, GAME_MAX, TILE_SIZE)

def get_random_position():
    return [
        randrange(*RANGE),
        randrange(*RANGE)
    ]

def get_free_position():
    position = get_random_position()

    while any(segment.collidepoint(position) for segment in segments):
        position = get_random_position()

    return position


snake = pg.rect.Rect(
    [0, 0, TILE_SIZE - 2, TILE_SIZE - 2]
)

snake.center = get_random_position()

length = 1

score = 0

segments = [snake.copy()]

snake_dir = (0, 0)


time, time_step = 0, 110


food = snake.copy()

food.center = get_free_position()

screen = pg.display.set_mode([WINDOW] * 2)
background_game = pg.image.load("assets/background_game.png").convert()
background_game = pg.transform.scale(background_game, (WINDOW, WINDOW))


clock = pg.time.Clock()


dirs = {
    pg.K_z: 1,
    pg.K_s: 1,
    pg.K_q: 1,
    pg.K_d: 1
}


game_stat = "menu"

play_button = pg.Rect(
    400,
    700,
    200,
    80
)


font_title = pg.font.Font(None, 120)
font_score = pg.font.Font(None, 50)
font_button = pg.font.Font(None, 50)


while True:

    for event in pg.event.get():

        if event.type == pg.QUIT:
            exit()

        if game_stat == "menu":

            if event.type == pg.MOUSEBUTTONDOWN:

                if play_button.collidepoint(event.pos):

                    game_stat = "game"


        if game_stat == "game":

            if event.type == pg.KEYDOWN:

                if event.key == pg.K_z and dirs[pg.K_z]:

                    snake_dir = (0, -TILE_SIZE)

                    dirs = {
                        pg.K_z: 1,
                        pg.K_s: 0,
                        pg.K_q: 1,
                        pg.K_d: 1
                    }


                if event.key == pg.K_s and dirs[pg.K_s]:

                    snake_dir = (0, TILE_SIZE)

                    dirs = {
                        pg.K_z: 0,
                        pg.K_s: 1,
                        pg.K_q: 1,
                        pg.K_d: 1
                    }


                if event.key == pg.K_q and dirs[pg.K_q]:

                    snake_dir = (-TILE_SIZE, 0)

                    dirs = {
                        pg.K_z: 1,
                        pg.K_s: 1,
                        pg.K_q: 1,
                        pg.K_d: 0
                    }


                if event.key == pg.K_d and dirs[pg.K_d]:

                    snake_dir = (TILE_SIZE, 0)

                    dirs = {
                        pg.K_z: 1,
                        pg.K_s: 1,
                        pg.K_q: 0,
                        pg.K_d: 1
                    }

    if game_stat == "menu":

        # Fond naturel
        screen.fill((18, 30, 18))

        # Zones de feuillage
        pg.draw.rect(
            screen,
            (22, 40, 20),
            pg.Rect(0, 0, WINDOW, 180)
        )

        pg.draw.rect(
            screen,
            (16, 27, 16),
            pg.Rect(0, 800, WINDOW, 200)
        )

        # Coins plus sombres
        pg.draw.circle(
            screen,
            (12, 22, 12),
            (0, 0),
            180
        )

        pg.draw.circle(
            screen,
            (12, 22, 12),
            (WINDOW, WINDOW),
            180
        )

        # Petites feuilles dans le fond
        leaf_light = (65, 130, 45)
        leaf_dark = (35, 85, 30)

        # Feuilles en haut à gauche
        pg.draw.circle(screen, leaf_dark, (70, 100), 18)
        pg.draw.circle(screen, leaf_light, (95, 80), 14)
        pg.draw.circle(screen, leaf_light, (55, 135), 12)

        # Petite tige
        pg.draw.line(
            screen,
            leaf_dark,
            (70, 100),
            (110, 65),
            4
        )

        # Feuilles en haut à droite
        pg.draw.circle(screen, leaf_dark, (930, 100), 18)
        pg.draw.circle(screen, leaf_light, (900, 75), 14)
        pg.draw.circle(screen, leaf_light, (950, 135), 12)

        # Petite tige
        pg.draw.line(
            screen,
            leaf_dark,
            (930, 100),
            (890, 65),
            4
        )

        # Feuilles en bas à gauche
        pg.draw.circle(screen, leaf_dark, (70, 850), 20)
        pg.draw.circle(screen, leaf_light, (100, 875), 14)
        pg.draw.circle(screen, leaf_light, (50, 900), 12)

        pg.draw.line(
            screen,
            leaf_dark,
            (70, 850),
            (110, 890),
            4
        )

        # Feuilles en bas à droite
        pg.draw.circle(screen, leaf_dark, (930, 850), 20)
        pg.draw.circle(screen, leaf_light, (900, 875), 14)
        pg.draw.circle(screen, leaf_light, (950, 900), 12)

        pg.draw.line(
            screen,
            leaf_dark,
            (930, 850),
            (890, 890),
            4
        )

        # Petits détails du fond
        detail_color = (35, 65, 30)

        pg.draw.circle(screen, detail_color, (250, 120), 4)
        pg.draw.circle(screen, detail_color, (760, 150), 5)
        pg.draw.circle(screen, detail_color, (100, 250), 4)
        pg.draw.circle(screen, detail_color, (900, 240), 5)

        pg.draw.circle(screen, detail_color, (110, 700), 4)
        pg.draw.circle(screen, detail_color, (890, 700), 4)
        pg.draw.circle(screen, detail_color, (300, 850), 5)
        pg.draw.circle(screen, detail_color, (700, 850), 4)

        frame = pg.Rect(150, 300, 700, 350)

        pg.draw.rect(screen, (35, 20, 10), frame.move(8, 8))

        # Bois extérieur
        pg.draw.rect(screen, (90, 55, 25), frame)

        # Bois intérieur
        pg.draw.rect(screen, (130, 80, 35), frame, 12)

        # Contour sombre
        pg.draw.rect(screen, (45, 25, 10), frame, 5)

        pg.draw.line(screen, (160, 100, 45), (180, 315), (400, 315), 3)
        pg.draw.line(screen, (70, 40, 18), (500, 635), (780, 635), 3)

        pg.draw.line(screen, (160, 100, 45), (165, 350), (165, 500), 3)
        pg.draw.line(screen, (70, 40, 18), (835, 400), (835, 570), 3)

        # Végétation autour du cadre
        leaf_color = (55, 120, 45)
        dark_leaf = (35, 80, 30)

        grid_rect = pg.Rect(175, 325, 650, 300)

        for x in range(grid_rect.left, grid_rect.right + 1, TILE_SIZE):
                pg.draw.line(
                    screen,
                    (45, 55, 40),
                    (x, grid_rect.top),
                    (x, grid_rect.bottom)
                )

        for y in range(grid_rect.top, grid_rect.bottom + 1, TILE_SIZE):
                pg.draw.line(
                    screen,
                    (45, 55, 40),
                    (grid_rect.left, y),
                    (grid_rect.right, y)
                )

        # Vigne en haut à gauche
        pg.draw.line(screen, dark_leaf, (160, 340), (120, 300), 5)
        pg.draw.circle(screen, leaf_color, (125, 305), 10)
        pg.draw.circle(screen, leaf_color, (145, 320), 8)

        # Vigne en haut à droite
        pg.draw.line(screen, dark_leaf, (840, 350), (880, 310), 5)
        pg.draw.circle(screen, leaf_color, (875, 315), 10)
        pg.draw.circle(screen, leaf_color, (855, 330), 8)

        # Petites feuilles en bas
        pg.draw.circle(screen, dark_leaf, (180, 665), 12)
        pg.draw.circle(screen, leaf_color, (205, 675), 9)
        pg.draw.circle(screen, dark_leaf, (820, 665), 12)
        pg.draw.circle(screen, leaf_color, (795, 675), 9)

        # Petite chenille décorative
        caterpillar_color = (90, 170, 60)
        caterpillar_dark = (45, 100, 30)

        # Corps
        pg.draw.circle(screen, caterpillar_dark, (430, 470), 18)
        pg.draw.circle(screen, caterpillar_color, (465, 470), 18)
        pg.draw.circle(screen, caterpillar_color, (500, 470), 18)

        # Tête
        pg.draw.circle(screen, caterpillar_color, (535, 470), 22)

        # Yeux
        pg.draw.circle(screen, (20, 20, 20), (528, 463), 4)
        pg.draw.circle(screen, (20, 20, 20), (542, 463), 4)

        # Feuille décorative
        leaf_color = (80, 150, 50)
        leaf_dark = (40, 90, 30)

        pg.draw.ellipse(
            screen,
            leaf_color,
            pg.Rect(590, 445, 45, 25)
        )

        pg.draw.line(
            screen,
            leaf_dark,
            (595, 463),
            (630, 453),
            3
        )


        title_shadow = font_title.render(
            "MOLT",
            True,
            (45, 25, 10)
        )

        title = font_title.render(
            "MOLT",
            True,
            (150, 95, 40)
        )

        title_rect = title.get_rect(
            center=(WINDOW // 2, 250)
        )

        screen.blit(
        title_shadow,
        title_rect.move(6, 6)
    )

        # Titre
        title_outline = font_title.render(
            "MOLT",
            True,
            (45, 25, 10)
        )

        for x, y in [
            (-3, 0),
            (3, 0),
            (0, -3),
            (0, 3),
        ]:
            screen.blit(
                title_outline,
                title_rect.move(x,y)
            )

        screen.blit(
            title,
            title_rect
        )

        mouse_pos = pg.mouse.get_pos()


        if play_button.collidepoint(mouse_pos):

            button_color = (145, 90, 40)

        else:

            button_color = (115, 70, 30)


        pg.draw.rect( 
            screen,
            (45, 25, 10),
            play_button.move(6, 6)
        )

        pg.draw.rect( 
            screen,
            button_color,
            play_button
        )

        pg.draw.rect( 
            screen,
            (45, 25, 10),
            play_button,
            5
        )

        pg.draw.line(
            screen,
            (175, 110, 50),
            (play_button.left + 15, play_button.top + 12),
            (play_button.right - 15, play_button.top + 12),
            3
        )

        text = font_button.render(
            "PLAY",
            True,
            (245, 225, 190)
        )

        text_rect = text.get_rect(
            center=play_button.center
        )

        screen.blit(
            text,
            text_rect
        )

    elif game_stat == "game":
        # Fond du jeu
        screen.blit(background_game, (0, 0))

        game_frame = pg.Rect(75, 75, 850, 850)

        # Ombre du cadre
        pg.draw.rect(
            screen,
            (35, 20, 10),
            game_frame.move(8, 8)
        )

        # Bois extérieur
        pg.draw.rect(
            screen,
            (90, 55, 25),
            game_frame
        )

        # Bois intérieur
        pg.draw.rect(
            screen,
            (130, 80, 35),
            game_frame,
            12
        )

        # Contour sombre
        pg.draw.rect(
            screen,
            (45, 25, 10),
            game_frame,
            5
        )

        # Grille
        game_grid = pg.Rect(100, 100, 800, 800)

        for x in range(game_grid.left, game_grid.right + 1, TILE_SIZE):
            pg.draw.line(
                screen,
                (45, 55, 40),
                (x, game_grid.top),
                (x, game_grid.bottom)
            )

        for y in range(game_grid.top, game_grid.bottom + 1, TILE_SIZE):
            pg.draw.line(
                screen,
                (45, 55, 40),
                (game_grid.left, y),
                (game_grid.right, y)
            )

        self_eating = pg.Rect.collidelist(
            snake,
            segments[:-1]
        ) != -1


        if (
            snake.left < 100
            or snake.right > 900
            or snake.top < 100
            or snake.bottom > 900
            or self_eating
        ):

            snake.center, food.center = get_random_position(), get_random_position()
            length, snake_dir = 1, (0, 0)
            score = 0
            segments = [snake.copy()]

        if any(segment.collidepoint(food.center) for segment in segments):

            food.center = get_free_position()

            length += 1
            score += 10

            if length >= MAX_LENGTH:
                game_stat = "win"

        pg.draw.rect(
            screen,
            'red',
            food
        )


        for segment in segments:

            pg.draw.rect(
                screen,
                'green',
                segment
            )


        time_now = pg.time.get_ticks()


        if time_now - time > time_step:

            time = time_now

            snake.move_ip(snake_dir)

            segments.append(
                snake.copy()
            )

            segments = segments[-length:]

        score_text = font_score.render(f"SCORE : {score}", True, (245, 225, 190))
        screen.blit(score_text, (120, 35))


    pg.display.flip()

    clock.tick(60)