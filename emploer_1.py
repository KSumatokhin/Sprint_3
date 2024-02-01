class Employee:
    # Аттрибут класса по умалчанию
    vacation_days = 28

    def __init__(self, first_name: str, second_name: str, gender: str):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender


# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee('Иван', 'Иванов', 'м')
employee2 = Employee('Симона', 'Авосева', 'ж')

# Допишите код для вывода информации о сотрудниках.
for employee in [employee1, employee2]:
    print(
        f'Имя: {employee.first_name}, '
        f'Фамилия: {employee.second_name}, '
        f'Пол: {employee.gender}, '
        f'Отпускных дней в году: {employee.vacation_days}.'
    )
