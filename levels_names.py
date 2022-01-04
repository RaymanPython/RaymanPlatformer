import pygame
import game


bg = pygame.image.load('image//bg1.png')


# Класс для расстановки платформ на сцене
class Level(object):
    def __init__(self, player):
        # Создаем группу спрайтов (поместим платформы различные сюда)
        self.platform_list = pygame.sprite.Group()

        self.lums_list = pygame.sprite.Group()
        self.lumsred_list = pygame.sprite.Group()
        self.minred_list = pygame.sprite.Group()
        self.finish_list = pygame.sprite.Group()
        # Ссылка на основного игрока
        self.player = player
        global classlist
        classlist = self

    # Чтобы все рисовалось, то нужно обновлять экран
    # При вызове этого метода обновление будет происходить
    def update(self):
        self.platform_list.update()
        self.lums_list.update()
        self.lumsred_list.update()
        self.finish_list.update()
        self.minred_list.update()

    # Метод для рисования объектов на сцене
    def draw(self, screen):
        # Рисуем задний фон
        screen.blit(bg, (0, 0))

        # Рисуем все платформы из группы спрайтов
        self.platform_list.draw(screen)
        self.lums_list.draw(screen)
        self.lumsred_list.draw(screen)
        self.minred_list.draw(screen)
        self.finish_list.draw(screen)


# Класс,, что описывает где будут находится все платформы
# на определенном уровне игры
class Level_01(Level):
    def __init__(self):
        # Вызываем родительский конструктор
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.size = [self.SCREEN_WIDTH, self.SCREEN_HEIGHT]
        player = game.Player()
        self.active_sprite_list = pygame.sprite.Group()
        self.levelind = 0
        # Создаем игрока

        player.level = self
        player.rect.x = 340
        player.rect.y = self.SCREEN_HEIGHT - player.rect.height
        self.active_sprite_list.add(player)

        Level.__init__(self, player)

        # Массив с данными про платформы. Данные в таком формате:
        # ширина, высота, x и y позиция
        level = [
            [210, 32, 500, 500, 0],
            [210, 32, 200, 400, 0],
            [210, 32, 600, 300, 0],
            [210, 32, 0, 300, 0],
            [210, 32, 210, 180, 0],
            [210, 32, 420, 200, 0],
            [210, 32, 630, 300, 0],
            [210, 32, 840, 300, 0],
            [210, 32, 1050, 300, 0],
            [210, 32, 1260, 300, 0],
            [210, 32, 1470, 300, 0],
            [210, 32, 1470, 250, 0],

        ]
        coin = [[1000, 200],
                [1000, 250]]

        coinred = [[300, 300]]

        minred = [[1470, 250]]

        finish = [10, 270]

        global lencoin, score
        lencoin = len(coin)
        for i in range(250):
            level.append([210, 32, (i - 250 // 2) * 210, 600, 0])

        colayder = game.Colad()
        colayder.player = player
        self.active_sprite_list.add(colayder)

        # Перебираем массив и добавляем каждую платформу в группу спрайтов - platform_list
        for platform in level:
            block = game.Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            if len(platform) == 5:
                block.rotate(platform[-1])
            self.platform_list.add(block)
            self.active_sprite_list.add(block)

        for lums in coin:
            lum = game.Lum()
            lum.rect.x = lums[0]
            lum.rect.y = lums[1]
            lum.player = self.player
            self.lums_list.add(lum)
            self.active_sprite_list.add(lum)

        for lums in coinred:
            lumred = game.Lumred()
            lumred.rect.x = lums[0]
            lumred.rect.y = lums[1]
            lumred.player = self.player
            self.lumsred_list.add(lumred)
            self.active_sprite_list.add(lumred)

        for lums in minred:
            min = game.Minred()
            min.rect.x = lums[0]
            min.rect.y = lums[1]
            min.player = self.player
            self.minred_list.add(min)
            self.active_sprite_list.add(min)

        fin = game.Finish()
        fin.rect.x = finish[0]
        fin.rect.y = finish[1]
        fin.player = self.player
        self.finish_list.add(fin)
        self.active_sprite_list.add(fin)


class Level_02(Level):
    def __init__(self):
        # Вызываем родительский конструктор
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.size = [self.SCREEN_WIDTH, self.SCREEN_HEIGHT]
        player = game.Player()
        self.active_sprite_list = pygame.sprite.Group()
        self.levelind = 0
        # Создаем игрока

        player.level = self
        player.rect.x = 340
        player.rect.y = self.SCREEN_HEIGHT - player.rect.height
        self.active_sprite_list.add(player)

        Level.__init__(self, player)

        # Массив с данными про платформы. Данные в таком формате:
        # ширина, высота, x и y позиция
        level = [
            [210, 32, 500, 500, 0],
            [210, 32, 200, 400, 0],
            [210, 32, 600, 300, 0],
            [210, 32, 0, 300, 0],
            [210, 32, 210, 180, 0],
            [210, 32, 420, 200, 0],
            [210, 32, 630, 300, 0],
            [210, 32, 840, 300, 0],
            [210, 32, 1050, 300, 0],
            [210, 32, 1260, 300, 0],
            [210, 32, 1470, 300, 0],
            [210, 32, 1470, 250, 0],

        ]
        coin = [[1000, 200],
                [1000, 250]]

        coinred = [[300, 300]]

        minred = [[1200, 250]]

        finish = [10, 270]

        global lencoin, score
        lencoin = len(coin)
        for i in range(250):
            level.append([210, 32, (i - 250 // 2) * 210, 600, 0])

        colayder = game.Colad()
        colayder.player = player
        self.active_sprite_list.add(colayder)

        # Перебираем массив и добавляем каждую платформу в группу спрайтов - platform_list
        for platform in level:
            block = game.Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            if len(platform) == 5:
                block.rotate(platform[-1])
            self.platform_list.add(block)
            self.active_sprite_list.add(block)

        for lums in coin:
            lum = game.Lum()
            lum.rect.x = lums[0]
            lum.rect.y = lums[1]
            lum.player = self.player
            self.lums_list.add(lum)
            self.active_sprite_list.add(lum)

        for lums in coinred:
            lumred = game.Lumred()
            lumred.rect.x = lums[0]
            lumred.rect.y = lums[1]
            lumred.player = self.player
            self.lumsred_list.add(lumred)
            self.active_sprite_list.add(lumred)

        for lums in minred:
            min = game.Minred()
            min.rect.x = lums[0]
            min.rect.y = lums[1]
            min.player = self.player
            self.minred_list.add(min)
            self.active_sprite_list.add(min)

        fin = game.Finish()
        fin.rect.x = finish[0]
        fin.rect.y = finish[1]
        fin.player = self.player
        self.finish_list.add(fin)
        self.active_sprite_list.add(fin)
