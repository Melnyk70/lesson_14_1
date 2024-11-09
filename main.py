class GroupFullException(Exception):
    """Виняток для ситуації, коли група переповнена."""
    pass

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender  # Зберігає стать людини
        self.age = age  # Зберігає вік людини
        self.first_name = first_name  # Зберігає ім'я людини
        self.last_name = last_name  # Зберігає прізвище людини

    def __str__(self):
        # Повертає рядок з основною інформацією про людину
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}'

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)  # Виклик ініціалізатора класу Human
        self.record_book = record_book  # Зберігає номер залікової книжки студента

    def __str__(self):
        # Повертає рядок з розширеною інформацією про студента
        return f'{super().__str__()}, Record Book: {self.record_book}'

class Group:
    def __init__(self, number):
        self.number = number  # Зберігає номер групи
        self.group = set()  # Ініціалізує пусту множину для студентів

    def add_student(self, student):
        if len(self.group) >= 10:  # Перевіряє, чи кількість студентів більше або дорівнює 10
            raise GroupFullException("Cannot add more than 10 students to the group")  # Порушує виняток, якщо студентів більше 10
        self.group.add(student)  # Додає студента до групи

    def delete_student(self, last_name):
        student = self.find_student(last_name)  # Знаходить студента по прізвищу
        if student:
            self.group.remove(student)  # Видаляє студента з групи, якщо знайдено

    def find_student(self, last_name):
        for student in self.group:  # Перебирає всіх студентів у групі
            if student.last_name == last_name:
                return student  # Повертає студента, якщо прізвище співпадає
        return None  # Повертає None, якщо студента не знайдено

    def __str__(self):
        # Створює рядок з інформацією про всіх студентів у групі
        all_students = ''.join(str(student) + '\n' for student in self.group)
        return f'Group Number: {self.number}\n{all_students}'  # Повертає номер групи та список студентів

# Створення студентів та групи
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')  # Створює екземпляр студента
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')  # Створює ще одного екземпляра студента
gr = Group('PD1')  # Створює екземпляр групи

# Додавання студентів до групи та обробка винятку
try:
    gr.add_student(st1)  # Додаєм першого студента до групи
    gr.add_student(st2)  # Додаєм другого студента до групи

    # Додавання клонів студентів Jobs і Taylor з унікальними ідентифікаторами
    gr.add_student(Student('Male', 31, 'Steve', 'Jobs-Clon1', 'AN146'))  # Додаєм клона Jobs
    gr.add_student(Student('Female', 26, 'Liza', 'Taylor-Clon1', 'AN147'))  # Додаєм клона Taylor
    gr.add_student(Student('Male', 32, 'Steve', 'Jobs-Clon2', 'AN148'))  # Додаєм клона Jobs
    gr.add_student(Student('Female', 27, 'Liza', 'Taylor-Clon2', 'AN149'))  # Додаєм клона Taylor
    gr.add_student(Student('Male', 33, 'Steve', 'Jobs-Clon3', 'AN150'))  # Додаєм клона Jobs
    gr.add_student(Student('Female', 28, 'Liza', 'Taylor-Clon3', 'AN151'))  # Додаєм клона Taylor
    gr.add_student(Student('Male', 34, 'Steve', 'Jobs-Clon4', 'AN152'))  # Додаєм клона Jobs
    gr.add_student(Student('Female', 29, 'Liza', 'Taylor-Clon4', 'AN153'))  # Додаєм клона Taylor

    # Спроба додати 11-го студента для тестування винятку
    gr.add_student(Student('Male', 35, 'Steve', 'Jobs-Clon5', 'AN154'))  # Додаєм клона Jobs, що має викликати виняток
except GroupFullException as e:
    print(e)  # Виводить повідомлення про виняток

print(gr)  # Виводить інформацію про групу та студентів