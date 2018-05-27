# Домашнее задание к лекции 1.5 «Практика по использованию циклов, коллекций и функций»

# Имеется группа студентов, у каждого из которых есть следующие характеристики:
# имя, фамилия, пол, предыдущий опыт в программировании (бинарная переменная),
# 5 оцененных по 10-бальной шкале домашних работ, оценка за экзамен по 10-балльной шкале.
# Необходимо написать программу, которая в зависимости от запроса пользователя будет выводить:
#
#     Среднюю оценку за домашние задания и за экзамен по всем группе в следующем виде:
#
# Средняя оценка за домашние задания по группе: X
# Средняя оценка за экзамен: Y
#
# где X и Y - вычисляемые значения;

# 2. Среднеюю оценку за домашние задания и за экзамен по группе в разрезе: а)пола б)наличия опыта в виде:
#
# Средняя оценка за домашние задания у мужчин: A
# Средняя оценка за экзамен у мужчин: B
# Средняя оценка за домашние задания у женщин: C
# Средняя оценка за экзамен у женщин: D
#
# Средняя оценка за домашние задания у студентов с опытом: E
# Средняя оценка за экзамен у студентов с опытом: F
# Средняя оценка за домашние задания у студентов без опыта: G
# Средняя оценка за экзамен у студентов без опыта: H
#
# где A, B, C, D, E, F, G, H - вычисляемые значения;

# 3. Определять лучшего студента, у которого будет максимальный балл по формуле
# 0.6 * его средняя оценка за домашние задания + 0.4 * оценка за экзамен в виде:
#
# Лучший студент: S с интегральной оценкой Z
#
# если студент один или:
#
# Лучшие студенты: S... с интегральной оценкой Z
#
# если студентов несколько, где S - имя/имена студентов, Z - вычисляемое значение.
# Студентов должно быть не менее 6.
# Код должен быть грамотно декомпозирован (максимально используйте функции).

students_list_source = [
    {'имя': 'Феопент', 'фамилия': 'Акакиев', 'пол': 'м', 'опыт': 'да', 'дз': [7, 5, 10, 6, 4], 'экзамен': [9]},
    {'имя': 'Еразм', 'фамилия': 'Зажрыщенко', 'пол': 'м', 'опыт': 'нет', 'дз': [2, 7, 6, 8, 5], 'экзамен': [10]},
    {'имя': 'Мацил', 'фамилия': 'Кошечек', 'пол': 'м', 'опыт': 'да', 'дз': [7, 4, 10, 6, 3], 'экзамен': [5]},
    {'имя': 'Щупл', 'фамилия': 'Собачек', 'пол': 'м', 'опыт': 'да', 'дз': [6, 8, 7, 6, 4], 'экзамен': [9]},
    {'имя': 'Епихария', 'фамилия': 'Питонова', 'пол': 'ж', 'опыт': 'нет', 'дз': [4, 5, 10, 7, 5], 'экзамен': [10]},
    {'имя': 'Кириякия', 'фамилия': 'Глухопердова', 'пол': 'ж', 'опыт': 'да', 'дз': [10, 6, 4, 9, 8], 'экзамен': [2]},
    {'имя': 'Мамбута', 'фамилия': 'Карлопутова', 'пол': 'ж', 'опыт': 'да', 'дз': [10, 6, 7, 10, 3], 'экзамен': [3]},
]

students_list = students_list_source.copy()


def help_commands():
    print('\n----------------------------------------------------\n'
          'Средняя оценка за домашние задания по группе: X\n'
          'Средняя оценка за экзамен: Y\n\n'
          'Средняя оценка за домашние задания у мужчин: A\n'
          'Средняя оценка за экзамен у мужчин: B\n\n'
          'Средняя оценка за домашние задания у женщин: C\n'
          'Средняя оценка за экзамен у женщин: D\n\n'
          'Средняя оценка за домашние задания у студентов с опытом: E\n'
          'Средняя оценка за экзамен у студентов с опытом: F\n\n'
          'Средняя оценка за домашние задания у студентов без опыта: G\n'
          'Средняя оценка за экзамен у студентов без опыта: H\n\n'
          'Лучший студент с интегральной оценкой: Z\n'
          '\nДля выхода нажмите  "q"\n'
          '----------------------------------------------------')


# print(help_commands())

def enter_cmd_x():
    user_input = input('Введите команду: ')
    return user_input.lower()


def average_score_from_group(students_list):
    """Средняя оценка за домашнее задание по группе"""
    average_score = 0
    for student in students_list:
        average_score += sum(student['дз']) / len(student['дз']) / len(students_list)
    return average_score


def average_score_exam(students_list):
    """Средняя оценка за экзамен"""
    average_exam = 0
    for student in students_list:
        average_exam += sum(student['экзамен']) / len(students_list)
    return average_exam


def average_score_home_sex(students_list, sex):
    """Средняя оценка за домашние задания мж"""
    average_home_sex = 0
    stud = 0
    for student in students_list:
        if student['пол'] == sex:
            average_home_sex += sum(student['дз']) / len(student['дз'])    # / len(student['пол'])
            stud += 1
    average_home_sex /= stud
    return average_home_sex


def average_score_exam_sex(students_list, sex):
    """Средняя оценка за экзамен мж"""
    average_exam_sex = 0
    stud = 0
    for student in students_list:
        if student['пол'] == sex:
            average_exam_sex += sum(student['экзамен'])
            stud += 1
    average_exam_sex /= stud
    return average_exam_sex


def average_score_home_experience(students_list, experience):
    """Средняя оценка за домашние задания у студентов с опытом, без опыта"""
    average_home_experience = 0
    stud = 0
    for student in students_list:
        if student['опыт'] == experience:
            average_home_experience += sum(student['дз']) / len(student['дз'])
            stud += 1
    average_home_experience /= stud
    return average_home_experience


def average_score_exam_experience(students_list, experience):
    """Средняя оценка за экзамен у студентов с опытом, без опыта"""
    average_exam_experience = 0
    stud = 0
    for student in students_list:
        if student['опыт'] == experience:
            average_exam_experience += sum(student['экзамен']) / len(student['экзамен'])
            stud += 1
    average_exam_experience /= stud
    return average_exam_experience


def best_student(students_list):
    """Лучший студент  с интегральной оценкой """
    best_score = 0
    best_stud = ''
    for student in students_list:
        best_stud_score_home = sum(student['дз']) / len(student['дз'])
        best_stud_score_exam = sum(student['экзамен'])
        integr = 0.6 * best_stud_score_home + 0.4 * best_stud_score_exam
        if integr > best_score:
            best_score = integr
            best_stud = '{имя} {фамилия}'.format(best_stud, **student)
    print('Лучший студент: {}   с интегральной оценкой {}'.format(best_stud, best_score))


def best_students(students_list):
    """Лучшие студенты  с интегральной оценкой """
    best_score = 0
    best_stud = ''
    best_list = []
    for student in students_list:
        best_stud_score_home = sum(student['дз']) / len(student['дз'])
        best_stud_score_exam = sum(student['экзамен'])
        integr = 0.6 * best_stud_score_home + 0.4 * best_stud_score_exam
        best_stud = '{имя} {фамилия}'.format(best_stud, **student)
        # best_list.append((integr, best_stud))
        if len(best_stud) > 1 and integr > best_score:
            best_list.append((integr, best_stud))
            print('Лучшие студенты: {}   с интегральной оценкой {}'.format(best_stud, best_score))

        # Исправить




        # elif len(best_stud) > 1:
        #     print('Лучшие студенты: {} с интегральной оценкой {}'.format(best_stud, best_score))
        # else:
        #     print('Лучший студент: {} с интегральной оценкой {}'.format(best_stud, best_score))
    # else:
    #     print('нет результата')

    # print('\tИнтегральная оценка студента: ', best_score)
    # return best_stud


def run():
    while True:
        help_commands()
        cmd = enter_cmd_x()

        if cmd == 'x':
            print('\tСредняя оценка за домашние задания по группе: ', (average_score_from_group(students_list)))
        elif cmd == 'y':
            print('\tСредняя оценка за экзамен: ', average_score_exam(students_list))
        elif cmd == 'a':
            print('\tСредняя оценка за домашние задания у мужчин: ', average_score_home_sex(students_list, 'м'))
        elif cmd == 'b':
            print('\tСредняя оценка за экзамен у мужчин: ', average_score_exam_sex(students_list, 'м'))
        elif cmd == 'c':
            print('\tСредняя оценка за домашние задания у женщин: ', average_score_home_sex(students_list, 'ж'))
        elif cmd == 'd':
            print('\tСредняя оценка за экзамен у женщин: ', average_score_exam_sex(students_list, 'ж'))
        elif cmd == 'e':
            print('\tСредняя оценка за домашние задания у студентов с опытом: ',
                  average_score_home_experience(students_list, 'да'))
        elif cmd == 'f':
            print('\tСредняя оценка за экзамен у студентов с опытом: ',
                  average_score_exam_experience(students_list, 'да'))
        elif cmd == 'g':
            print('\tСредняя оценка за домашние задания у студентов без опыта: ',
                  average_score_home_experience(students_list, 'нет'))
        elif cmd == 'h':
            print('\tСредняя оценка за экзамен у студентов без опыта: ',
                  average_score_exam_experience(students_list, 'нет'))
        elif cmd == 'z':
            best_student(students_list)
            # print('\tЛучший студент: ', best_student(students_list))
        elif cmd == 's':
            best_students(students_list)

        elif cmd == 'q':
            break
        else:
            print('\n Не попали по кнопке. Цельтесь лучше!')


run()
print('\tЗакончили упражнение. Пока!')