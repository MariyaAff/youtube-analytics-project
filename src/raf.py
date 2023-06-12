import json


class Raf9:
    def __init__(self):
        self.ingredients = ['lemon', 'mint', 'ice', 'orange', 'soda', 'tomato']
        self.get_coctails_from_db()

    def __call__(self, *args, **kwargs):
        while True:
            self.__help_text()
            command = input('Введите команду:')
            if command == '0':
                print('Всего хорошего! Приходите еще!')
                break
            elif command == '1':
                current_ings = self.choose_ingredients()
                chose_coctail = self.find_coctail(current_ings)
                if chose_coctail is None:
                    self.save_coctail(current_ings)
                else:
                    print(f'You choose {chose_coctail} coctail')
            else:
                print('Нет такой команды')

    def __help_text(self):
        print('Доступны команды:')
        print('1 - выбрать ингридиенты')
        print('0 - выход')

    def save_coctail(self, current_ings):
        self.coctails.append({
            'name': 'unnamed',
            'ingredients': current_ings
        })

        with open('coctails.json', 'r') as json_file:
            json.dump(self.coctails, json_file)

    def get_coctails_from_db(self):
        with open('coctails.json', 'r') as json_file:
            self.coctails = json.load(json_file)

    def find_coctail(self, current_ings):
        for c in self.coctails:
            if c.get('ingredients') == current_ings:
                return c.get('name')

        return None

    def choose_ingredients(self):
        chose_ings = []
        print('Список ингредиентов: ')
        i = 0
        for ing in self.ingredients:
            i += 1
            print(f'{i}. {ing}')

        print('0 - для выхода')

        while True:
            command = input('Введите команду:')
            if command == '0':
                return chose_ings

            else:
                if command.isdigit():
                    number = int(command)
                    if number >= len(self.ingredients):
                        print('Такого ингридиента в списке нет')
                    else:
                        chose_ings.append(self.ingredients[number - 1])
                else:
                    print('Введите НОМЕР ингредиента')


if __name__ == '__main__':
    raf9 = Raf9()  # Инициализация класса
    raf9()  # Вызов класса
