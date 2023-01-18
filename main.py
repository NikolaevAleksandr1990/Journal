class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def add_courses_in_progress(self, course_name):
        self.courses_in_progress.append(course_name)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _avr_grades(self):
        avg = []
        for value in self.grades.values():
            avg.extend(value)
        res_ = sum(avg) / len(avg)
        return round(res_, 2)

    def courses_in_progress_(self):
        result = ', '.join(self.courses_in_progress)
        return result

    def finished_courses_(self):
        result = ', '.join(self.finished_courses)
        return result

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}' \
              f' \nСредняя оценка за домашние задания: {self._avr_grades()} \nКурсы в процессе изучения:' \
              f' {self.courses_in_progress_()} \nЗавершенные курсы: {self.finished_courses_()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не найден в списке лекторов.')
            return
        return self._avr_grades < other._avr_grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _avr_grades(self):
        avg = []
        for value in self.grades.values():
            avg.extend(value)
        res_ = sum(avg) / len(avg)
        return round(res_, 2)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}' \
              f' \nСредняя оценка за лекции: {self._avr_grades()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не найден в списке лекторов.')
            return
        return self._avr_grades < other._avr_grades


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['ty']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

one_lecturer = Lecturer('Rock', 'Ice')
one_lecturer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_lec(one_lecturer, 'Python', 9)
best_student.rate_lec(one_lecturer, 'Python', 4)
best_student.add_courses('Git')
best_student.add_courses_in_progress('JS')

print(best_student.grades)
print(one_lecturer.grades)
print(cool_reviewer)
print(one_lecturer)
print(best_student)
