import  pygame
import game
import levels_names

def go_level(levelind=0):
    levels = [levels_names.Level_01, levels_names.Level_02]
    # qslevelind = 1

    # Создаем все уровни
    level_list = []
    level_list.append(levels[levelind]())

    # Устанавливаем текущий уровень
    current_level_no = 0
    current_level = level_list[current_level_no]
    game.main(current_level)


class Adventher:

    def __init__(self):
        pass


class Level(pygame.sprite.Sprite):

    def __init__(self, name):
        # Конструктор платформ
        super().__init__()

        # Также указываем фото платформы
        self.image = pygame.image.load('image//portal1.png')
        self.name = name
        # Установите ссылку на изображение прямоугольника
        self.rect = self.image.get_rect()

    def update(self, *arg):
        if len(arg) == 1:
            pos = arg[0]
            if self.rect.collidepoint(pos):
                global level_name
                level_name = self.name


def main():
    pygame.init()

    # Установка высоты и ширины
    bg = pygame.image.load('image//bg1.png')

    size = (700, 800)
    screen = pygame.display.set_mode(size)
    # screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    # Название игры
    pygame.display.set_caption("Платформер")

    # Цикл будет до тех пор, пока пользователь не нажмет кнопку закрытия
    done = True

    # Используется для управления скоростью обновления экрана
    clock = pygame.time.Clock()

    soundfon = pygame.mixer.music.load('fon1.mp3')
    pygame.mixer.music.set_volume(-1)
    # pygame.mixer.music.play()
    # Основной цикл программы
    sprite_list = pygame.sprite.Group()
    while done:
        # Отслеживание действий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Если закрыл программу, то останавливаем цикл
                done = False
                quit()
            # Если нажали на стрелки клавиатуры, то двигаем объект
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()

            if event.type == pygame.KEYUP:
                pass

        # Обновляем игрока
        sprite_list.update()
        clock.tick(30)
        # Обновляем экран после рисования объектов
        pygame.display.flip()
        screen.blit(bg, (0, 0))


go_level(0)
