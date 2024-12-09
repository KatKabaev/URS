# создание системы регистрации пользователя

class Database:
    '''
    База данных для хранения имени пользователя и пароля.
    '''
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль.
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input('Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n'))  # В этом была проблема (int) очень важно, возможно 1 и 2 воспринимались как строки
        if choice == 1:
            login = input('Введите логин: ')
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f'Добро пожаловать, {login}!')
                    break
                else:
                    print("Пользователь ввел неверный пароль")
            else:
                print('Пользователь не найден')
        if choice == 2:
            user = User(input('Введите логин: '), password := input("Введите пароль: "),
                        password2 := input("Повторите пароль: "))
            if password != password2:
                print("Пароли не совпадают, попробуйте еще раз")
                continue
            database.add_user(user.username, user.password)
            print(f'Данные в словаре: {database.data}')
