class Student:
    """
    Initializes the object with the provided name, surname, and gender.

    Parameters:
        name (str): The name of the person.
        surname (str): The surname of the person.
        gender (str): The gender of the person ('male' or 'female').
    Returns:
        None
    """
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_for_lectures:
                lecturer.grades_for_lectures[course] += [grade]
            else:
                lecturer.grades_for_lectures[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = self.average_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg_grade}\n'
                f'Курсы в процессе изучения: {courses_in_progress_str}\n'
                f'Завершенные курсы: {finished_courses_str}')

    def average_grade(self):
        total = []
        for grades in self.grades.values():
            total.extend(grades)
        return round(sum(total) / len(total), 1) if total else 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()


class Mentor:
    """
    Initializes the object with the given name and surname.

    Parameters:
        name (str): The name of the person.
        surname (str): The surname of the person.

    Returns:
        None
    """
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_for_lectures = {}

    def __str__(self):
        avg_grade = self.average_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}'

    def average_grade(self):
        total = []
        for grades in self.grades_for_lectures.values():
            total.extend(grades)
        return round(sum(total) / len(total), 1) if total else 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_grade_for_students(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return round(sum(total_grades) / len(total_grades), 1) if total_grades else 0


def average_grade_for_lecturers(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades_for_lectures:
            total_grades.extend(lecturer.grades_for_lectures[course])
    return round(sum(total_grades) / len(total_grades), 1) if total_grades else 0


# Создание экземпляров студентов
student1 = Student('Denis', 'Erokhin', 'male')
student1.finished_courses += ['Введение в программирование']
student1.courses_in_progress += ['Python', 'Git']
student2 = Student('Lara', 'Croft', 'female')
student2.courses_in_progress += ['Python']
student2.finished_courses += []

# Создание экземпляров лекторов
lecturer1 = Lecturer('Spider', 'Man')
lecturer1.courses_attached += ['Python']
lecturer2 = Lecturer('Doctor', 'Who')
lecturer2.courses_attached += ['Git']

# Создание экземпляров проверяющих
reviewer1 = Reviewer('John', 'Konnor')
reviewer1.courses_attached += ['Python']
reviewer2 = Reviewer('James', 'Bond')
reviewer2.courses_attached += ['Git']

# Выставление оценок студентам
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student1, 'Git', 8)
reviewer2.rate_hw(student2, 'Git', 7)

# Выставление оценок лекторам
student1.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Python', 9)
student1.rate_lecturer(lecturer2, 'Git', 8)
student2.rate_lecturer(lecturer1, 'Git', 9)

# Вывод информации о студентах, лекторах и проверяющих
print(f'________\nСТУДЕНТЫ:\n\n{student1}\n\n{student2}')
print(f'\n________\nЛЕКТОРЫ:\n\n{lecturer1}\n\n{lecturer2}')
print(f'\n________\nПРОВЕРЯЮЩИЕ:\n\n{reviewer1}\n\n{reviewer2}\n')


# Сравнение лекторов и студентов (Зачем? Чтобы что?)
if lecturer1 > lecturer2:
    print(f'Лектор {lecturer1.name} {lecturer1.surname} по баллам лучше лектора {lecturer2.name} {lecturer2.surname}')
else:
    print(f'Лектор {lecturer1.name} {lecturer1.surname} не лучше лектора {lecturer2.name} {lecturer2.surname}')

if student1 > student2:
    print(f'Студент {student1.name} {student1.surname} по баллам лучше студента {student2.name} {student2.surname}')
else:
    print(f'Студент {student1.name} {student1.surname} не лучше студента {student2.name} {student2.surname}\n')

# print(lecturer1 > lecturer2)
# print(student1 < student2)

# Вывод средних оценок
print('Средние оценки:')
print(average_grade_for_students([student1, student2], 'Python'))
print(average_grade_for_lecturers([lecturer1, lecturer2], 'Git'))
