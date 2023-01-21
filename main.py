class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avr_grades = 0

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
        self.avr_grades = round(res_, 2)
        return round(res_, 2)

    def _courses_in_progress_(self):
        result = ', '.join(self.courses_in_progress)
        return result

    def _finished_courses_(self):
        result = ', '.join(self.finished_courses)
        return result

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}' \
              f' \nСредняя оценка за домашние задания: {self._avr_grades()} \nКурсы в процессе изучения:' \
              f' {self._courses_in_progress_()} \nЗавершенные курсы: {self._finished_courses_()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не найден в списке студентов.')
            return
        return self.avr_grades < other.avr_grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avr_grades = 0

    def _avr_grades(self):
        avg = []
        for value in self.grades.values():
            avg.extend(value)
        res_ = sum(avg) / len(avg)
        self.avr_grades = round(res_, 2)
        return round(res_, 2)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}' \
              f' \nСредняя оценка за лекции: {self._avr_grades()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не найден в списке лекторов.')
            return
        return self.avr_grades < other.avr_grades


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


def avr_to_course(course, student_list):
    sum_rating = 0
    quan_rating = 0
    for stud in student_list:
        if course in stud.grades:
            stud_sum_rating = stud.grades[course]
            sum_rating += sum(stud_sum_rating)
            quan_rating += len(list(stud.grades[course]))
    avr_rating = round(sum_rating / quan_rating, 2)
    res = f'Средняя оценка студентов за курс {course} равна: {avr_rating}'
    return res


def avr_to_course_lecturer(course, lecturer_list):
    sum_rating = 0
    quan_rating = 0
    for lectr in lecturer_list:
        if course in lectr.grades:
            stud_sum_rating = lectr.grades[course]
            sum_rating += sum(stud_sum_rating)
            quan_rating += len(list(lectr.grades[course]))
    avr_rating = round(sum_rating / quan_rating, 2)
    res = f'Средняя оценка лекторов за курс {course} равна: {avr_rating}'
    return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.add_courses('Git')

lose_student = Student('Rick', 'Sanchos', 'male')
lose_student.courses_in_progress += ['Python']
lose_student.courses_in_progress += ['Java']
lose_student.add_courses('C++')

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Java']

super_reviewer = Reviewer('Nick', 'Bones')
super_reviewer.courses_attached += ['Java']
super_reviewer.courses_attached += ['Python']

one_lecturer = Lecturer('Rock', 'Ice')
one_lecturer.courses_attached += ['Python']
one_lecturer.courses_attached += ['Java']

two_lecturer = Lecturer('Sam', 'Jones')
two_lecturer.courses_attached += ['Python']
two_lecturer.courses_attached += ['Java']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Java', 10)
cool_reviewer.rate_hw(lose_student, 'Python', 10)
super_reviewer.rate_hw(lose_student, 'Java', 3)
super_reviewer.rate_hw(best_student, 'Java', 10)
super_reviewer.rate_hw(lose_student, 'Python', 1)

best_student.rate_lec(one_lecturer, 'Python', 9)
best_student.rate_lec(two_lecturer, 'Java', 4)
lose_student.rate_lec(one_lecturer, 'Python', 8)
lose_student.rate_lec(one_lecturer, 'Java', 5)

print(best_student)
print(lose_student)
print(one_lecturer)
print(two_lecturer)
print(cool_reviewer)
print(super_reviewer)
print(best_student < lose_student)
print(one_lecturer > two_lecturer)
print(avr_to_course('Python', student_list=[best_student, lose_student]))
print(avr_to_course_lecturer('Java', lecturer_list=[one_lecturer, two_lecturer]))
