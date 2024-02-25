class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if (0 < grade <= 10):
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка: оценка по 10-ти бальной системе'
        else:
            return 'Ошибка'

    def __average(self) -> float:
        average = 0
        count = 0
        for v in self.grades.values():
            count += 1
            average += sum(v) / v.count()

        if (count == 0):
            return 0
        else:
            average = average / count
            return average

    def __eq__(self, other) -> bool:
        return self.__average() == other.__average()

    def __lt__(self, other) -> bool:
        return self.__average() < other.__average()

    def __str__(self) -> str:
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname + '\nСредняя оценка за домашние задания: ' \
            + str(self.__average()) \
            + '\nКурсы в процессе изучения: ' + ", ".join(self.courses_in_progress) \
            + '\nЗавершенные курсы: ' + ", ".join(self.finished_courses)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __average(self) -> float:
        average = 0
        count = 0
        for v in self.grades.values():
            count += 1
            average += sum(v) / v.count()

        if (count == 0):
            return 0
        else:
            average = average / count
            return average

    def __eq__(self, other) -> bool:
        return self.__average() == other.__average()

    def __lt__(self, other) -> bool:
        return self.__average() < other.__average()

    def __str__(self) -> str:
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname + '\nСредняя оценка за лекции: ' + str(
            self.__average())


class Reviewer(Mentor):

    def __str__(self) -> str:
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_list = [Student('Иван', 'Иванов', 20), Student('Петр', 'Петров', 22)]
lecturer_list = [Lecturer('Сидор', 'Сидоров'), Lecturer('Василий', 'Василье')]
ReviewerPavlov = Reviewer('Павел', 'Павлов')
ReviewerSergeev = Reviewer('Сергей', 'Сергеев')


def student_average_grade_of_course(course, list):
    average = 0
    for st in list:
        average += st.grades[course]

    return average / list.count()


def lecturer_average_grade_of_course(course, list):
    average = 0
    for st in list:
        average += sum(st.grades[course]) / st.grades[course].count()

    return average / list.count()


print(student_list[0])
print(lecturer_list[0])