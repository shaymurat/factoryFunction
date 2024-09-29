from random import choice

# ----------------- Lambda-функция ----------------------

first = 'Мама мыла раму'
second = 'Рамена мало было'

# список совпадения букв в той же позиции
print(list(map(lambda x, y: x == y, first, second)))

# -------------------- Замыкание ------------------------


def get_advanced_writer(file_name):
    '''Возвращает функцию для добавления в файл построчно всех данных'''
    def write_everything(*data_set):
        with open(file_name, 'w') as f:
            for data in data_set:
                f.write(f'{data}\n')
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# ---------------------- Метод __call__ ----------------------


class MysticBall:
    '''
    Вызываемый класс
    Возвращает случайно выбранный элемент из коллекции
    '''

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
