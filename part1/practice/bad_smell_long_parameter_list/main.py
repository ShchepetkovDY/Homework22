# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def move(self, field, x_coord, y_coord, direction, is_fly, crawl, speed = 1):

        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGTH':
                new_y = y_coord
                new_x = x_coord + speed
        if crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGTH':
                new_y = y_coord
                new_x = x_coord + speed

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...

class Unit:
    def __init__(self, field, x_coord: int, y_coord: int, direction, is_fly: bool, is_crawl: bool, speed: int = 1):
        self.field = field
        self.x_cord = x_coord
        self.y_cord = y_coord
        self.direction = direction
        self.is_fly = is_fly
        self.is_crawl = is_crawl
        self.speed = speed

    def get_speed(self):
        if self.is_fly and self.is_crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        elif self.is_fly:
            self.speed *= 1.2

        elif self.is_crawl:
            self.speed *= 0.5

    def move(self, direction):
        speed = self.get_speed()
        if direction == 'UP':
            new_y = self.y_coord + speed
            new_x = self.x_coord
        elif direction == 'DOWN':
            new_y = self.y_coord - speed
            new_x = self.x_coord
        elif direction == 'LEFT':
            new_y = self.y_coord
            new_x = self.x_coord - speed
        elif direction == 'RIGTH':
            new_y = self.y_coord
            new_x = self.x_coord + speed
        self.field.set_unit(x=new_x, y=new_y, unit=self)
