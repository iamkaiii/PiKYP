import pygame
import sys

# Инициализация Pygame
pygame.init()

#Звуковые эффекты
pygame.mixer.music.load("hooray.mp3")

# Константы
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_SIZE = 3
SQUARE_SIZE = WIDTH // BOARD_SIZE

# Цвета

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (215, 71, 96)
LINE_COLOR = WHITE

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")


# Игровое поле
board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def draw_board():
    for row in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (row * SQUARE_SIZE, 0), (row * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def draw_symbol(row, col, symbol):
    font = pygame.font.Font(None, 100)
    text = font.render(symbol, True, WHITE)
    text_rect = text.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
    screen.blit(text, text_rect)


def check_winner(symbol):
    for i in range(BOARD_SIZE):
        if all(board[i][j] == symbol for j in range(BOARD_SIZE)) or all(board[j][i] == symbol for j in range(BOARD_SIZE)):
            return True
    # Проверка по диагоналям
    if all(board[i][i] == symbol for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - 1 - i] == symbol for i in range(BOARD_SIZE)):
        return True
    return False


current_symbol = 'X'
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col = x // SQUARE_SIZE
            row = y // SQUARE_SIZE

            if board[row][col] == '':
                board[row][col] = current_symbol
                if check_winner(current_symbol):
                    print(f"Игрок {current_symbol} победил!")
                    game_over = True
                elif all(board[i][j] != '' for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)):
                    print("Ничья!")
                    game_over = True
                else:
                    current_symbol = 'O' if current_symbol == 'X' else 'X'

    # Отрисовка фона
    screen.fill(PINK)

    # Отрисовка игрового поля
    draw_board()

    # Отрисовка символов
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] != '':
                draw_symbol(i, j, board[i][j])

    # Обновление дисплея
    pygame.display.flip()

    # Проверка на окончание игры
    if game_over:
        font = pygame.font.Font('better-vcr-5.2.ttf', 22)

        if current_symbol != 'X':
            pygame.mixer.music.play(0, 6.5, 0)
            screen.fill(PINK)
            text = font.render("Победил игрок O!", True, WHITE)
        else:
            pygame.mixer.music.play(0, 6.5, 0)
            screen.fill(PINK)
            text = font.render("Победил игрок X!", True, WHITE)

        if all(board[i][j] != '' for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)):
            text = font.render("Ничья!", True, WHITE)
            screen.fill(PINK)

        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3800)
        pygame.quit()
        sys.exit()