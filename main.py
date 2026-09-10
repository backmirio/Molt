import pygame as pg

from random import randrange

pg.init()

WINDOW = 1000

TILE_SIZE = 50

RANGE = (
    TILE_SIZE // 2,
    WINDOW - TILE_SIZE // 2,
    TILE_SIZE
)

get_random_position = lambda: [
    randrange(*RANGE),
    randrange(*RANGE)
]


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

food.center = get_random_position()


screen = pg.display.set_mode([WINDOW] * 2)

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
    650,
    200,
    80
)


font_title = pg.font.Font(None, 120)

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

        screen.fill((15, 15, 15))

        title = font_title.render(
            "MOLT",
            True,
            (255, 255, 255)
        )

        title_rect = title.get_rect(
            center=(WINDOW // 2, 250)
        )

        screen.blit(title, title_rect)

        mouse_pos = pg.mouse.get_pos()


        if play_button.collidepoint(mouse_pos):

            button_color = (130, 200, 70)

        else:

            button_color = (100, 170, 50)


        pg.draw.rect(
            screen,
            button_color,
            play_button
        )


        pg.draw.rect(
            screen,
            (255, 255, 255),
            play_button,
            4
        )

        text = font_button.render(
            "PLAY",
            True,
            (255, 255, 255)
        )

        text_rect = text.get_rect(
            center=play_button.center
        )

        screen.blit(
            text,
            text_rect
        )

    elif game_stat == "game":

        screen.fill('black')

        for x in range(0, WINDOW, TILE_SIZE):

            pg.draw.line(
                screen,
                (30, 30, 30),
                (x, 0),
                (x, WINDOW)
            )


        for y in range(0, WINDOW, TILE_SIZE):

            pg.draw.line(
                screen,
                (30, 30, 30),
                (0, y),
                (WINDOW, y)
            )

        font_score = pg.font.Font(None,40)

        score_text = font_score.render(
            f"Score : {score}",
            True,
            (255, 255, 255)
        )

        screen.blit(
            score_text,
            (20, 20)
        )

        self_eating = pg.Rect.collidelist(
            snake,
            segments[:-1]
        ) != -1


        if (
            snake.left < 0
            or snake.right > WINDOW
            or snake.top < 0
            or snake.bottom > WINDOW
            or self_eating
        ):

            snake.center, food.center = get_random_position(), get_random_position()
            length, snake_dir = 1, (0, 0)
            score = 0
            segments = [snake.copy()]

        if snake.center == food.center:

            food.center = get_random_position()

            length += 1
            score += 10


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


    pg.display.flip()

    clock.tick(60)