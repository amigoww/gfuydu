class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        married_status = "женат/замужем" if self.is_married else "не женат/не замужем"
        print(f"Меня зовут {self.full_name}. Мне {self.age} лет. Я {married_status}.")


class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_grade(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)


class Teacher(Person):
    base_salary = 30000  # базовая зарплата

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        if self.experience <= 3:
            return self.base_salary
        return self.base_salary + (self.base_salary * 0.05 * (self.experience - 3))


# Создаем объект учителя
teacher = Teacher("Иван Петров", 45, True, 10)
teacher.introduce_myself()
print(f"Зарплата учителя: {teacher.calculate_salary()} рублей.\n")

# Функция для создания учеников
def create_students():
    student1 = Student("Ольга Иванова", 16, False, {"Математика": 5, "Физика": 4, "История": 3})
    student2 = Student("Алексей Смирнов", 17, False, {"Математика": 3, "Физика": 4, "История": 5})
    student3 = Student("Мария Кузнецова", 16, False, {"Математика": 4, "Физика": 5, "История": 4})
    return [student1, student2, student3]

# Создаем студентов и распечатываем информацию о каждом
students = create_students()
for student in students:
    student.introduce_myself()
    for subject, mark in student.marks.items():
        print(f"{subject}: {mark}")
    print(f"Средняя оценка: {student.average_grade():.2f}\n")