import random

# Список для хранения предметов в инвентаре игрока
inventory = []

# Словарь для хранения информации о персонажах
characters = {
    "герой": "волшебник",
    "противник": "дракон",
}

# Функция для вывода текста с использованием f-строк
def print_story(text):
    print(f"~ {text} ~")

# Функция для обработки выбора игрока
def make_choice(choices):
    print("Выберите действие:")
    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")
    while True:
        try:
            choice = int(input("Ваш выбор: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Пожалуйста, введите корректный номер выбора.")
        except ValueError:
            print("Пожалуйста, введите число.")

# Функция для обработки боя с драконом
def dragon_battle():
    print_story("Вы вступили в бой с драконом!")
    if "меч" in inventory:
        print_story("С мечом в руках вы победили дракона!")
        print_story("Вы спасли королевство!")
    else:
        print_story("У вас нет меча. Дракон сжег вас огнем. Игра окончена.")
        exit()

# Функция для основного сюжета игры
def main_story():
    print_story("Добро пожаловать в мир волшебства!")
    print_story(f"Вы - молодой {characters['герой']}. Вам предстоит спасти королевство от {characters['противник']}а.")

    choice1 = make_choice(["Продолжить путь в лес.", "Идти к горам."])

    if choice1 == 1:
        print_story("Вы отправились в лес и встретили фею.")
        print_story("Фея дарует вам магический посох.")
        inventory.append("посох")
    else:
        print_story("Вы направились к горам, но на пути вас атаковал дракон.")
        dragon_battle()

    print_story("Теперь у вас есть выбор: идти в пещеру дракона или вернуться в деревню.")
    choice2 = make_choice(["Идти в пещеру дракона.", "Вернуться в деревню."])

    if choice2 == 1:
        print_story("Вы вошли в пещеру дракона.")
        if "посох" in inventory:
            print_story("С посохом в руках вы смогли победить дракона!")
            print_story("Поздравляем! Вы спасли королевство!")
        else:
            print_story("У вас нет подходящего оружия. Дракон уничтожил вас. Игра окончена.")
            exit()
    else:
        print_story("Вы вернулись в деревню и обнаружили меч в магазине.")
        choice3 = make_choice(["Купить меч.", "Покинуть магазин."])

        if choice3 == 1:
            print_story("Теперь у вас есть меч.")
            inventory.append("меч")
            choice4 = make_choice(["Вернуться в деревню.", "Идти к пещере дракона."])

    if choice4 == 1:
        print_story("Вы решили вернуться в деревню.")
        print_story("Но вас атаковал дракон.")
        dragon_battle()
    else:
        print_story("Вы решили покинуть магазин и вернуться в деревню.")
        print_story("Но вас атаковал дракон.")
        dragon_battle()
# Функция для обработки победы над драконом после покупки меча
def defeat_dragon_with_sword():
    print_story("Вы вернулись к пещере дракона, вооружившись мечом.")
    print_story("С мечом в руках вы смогли победить дракона!")
    print_story("Поздравляем! Вы спасли королевство!")

# Запуск игры
if __name__ == "__main__":
    main_story()