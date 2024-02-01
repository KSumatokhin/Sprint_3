class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')

    def dial_type_upgrade(self, new_dial_type):
        self.dial_type = new_dial_type

    # Вот он - магический метод __str__ с пользовательским описанием.
    def __str__(self):
        return f'Это {self.line_type} телефон. Набор - {self.dial_type}.'


# Дочерний класс, унаследованный от класса Phone.
class MobilePhone(Phone):
    # Переопределить значение атрибута line_type класса Phone.
    line_type = 'беспроводной'
    battery_type = 'Li-ion'

    def __init__(self, dial_type_value, network_type):
        # Новый атрибут объекта.
        self.network_type = network_type
        # Вызов родительского конструктора.
        super().__init__(dial_type_value)

    # Переопределить метод ring() класса Phone.
    def ring(self):
        print('Дзынь-Дзынь!')

    # Новый метод.
    def start_game(self):
        print('Игра запущена')


rotary_phone = Phone('дисковый')
mobile_phone = MobilePhone('сенсорный', 'LTE')

print(mobile_phone)
