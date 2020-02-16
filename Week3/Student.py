import random
import csv
import matplotlib.pyplot as plt
import pandas as pd


class Student():

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_grades_avg(self):
        grade_sum = sum(self.data_sheet.get_grades())
        grade_len = len(self.data_sheet.get_grades())
        return grade_sum/grade_len

    def get_etcs_progress(self):
        etcs_sum = float(self.data_sheet.get_etcs_points())
        etcs_progress = (etcs_sum/150)*100
        return etcs_progress


class DataSheet():

    def __init__(self, course_list):
        self.course_list = course_list

    def get_grades(self):
        grades = []
        for course in self.course_list:
            if course.grade != None:
                grades.append(int(course.grade))
        return grades

    def get_etcs_points(self):
        etcs_points = 0
        for course in self.course_list:
            if course.grade != None:
                etcs_points += int(course.etcs)
        return etcs_points


class Course():

    def __init__(self, name, teacher, etcs, classroom, grade=None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.etcs = etcs
        self.grade = grade


def get_random_courses():
    grade_list = [-3, 0, 2, 4, 7, 10, 12]
    course1 = Course("Mathematics", "Bob",
                     "15", "101", random.choice(grade_list))
    course2 = Course("English", "Martha",
                     "10", "123", random.choice(grade_list))
    course3 = Course("Physics", "Simon",
                     "10", "010", random.choice(grade_list))
    course4 = Course("Music", "Asta",
                     "5", "004", random.choice(grade_list))
    course5 = Course("Programming", "Lars",
                     "30", "114", random.choice(grade_list))
    course6 = Course("French", "Henry",
                     "20", "090", random.choice(grade_list))
    course_list = [course1, course2, course3, course4, course5, course6]
    lst_courses = []
    for i in range(0, 6):
        lst_courses.append(random.choice(course_list))
    return lst_courses


def create_students(amount):
    names = ["Lee", "Kim", "Sam", "Bob", "Donald",
             "Simon", "Richard", "Lars", "Thomas", "John"]
    genders = ["Male", "Female"]
    img_url = ["img/123", "img/091", "img/450"]

    students = []
    for i in range(amount):
        students.append(Student(random.choice(names), random.choice(
            genders), DataSheet(get_random_courses()), random.choice(img_url)))
    return students


def write_to_csv(path, lst_students):
    with open(path, 'w') as file_object:
        for student in lst_students:
            file_object.write(student.name + ",")
            for course in student.data_sheet.course_list:
                file_object.write(course.name + ",")
                file_object.write(course.teacher + ",")
                file_object.write(course.etcs + ",")
                file_object.write(course.classroom + ",")
                if course.grade != None:
                    file_object.write(str(course.grade) + ",")
                else:
                    file_object.write("None" + ",")
            file_object.write(student.image_url + "\n")


def read_from_csv(path):

    student_lst = []
    with open(path) as f:
        reader = csv.reader(f)
        for line in reader:
            counter = 0
            course_list = []
            while (counter != -1 or counter > 100):
                print("##############################################")
                print(line[counter+1])
                print(line[counter+2])
                print(line[counter+3])
                print(line[counter+4])
                print(line[counter+5])
                course = Course(line[counter+1], line[counter+2],
                                line[counter+3], line[counter+4], line[counter+5])
                counter += 5
                course_list.append(course)
                if ("img" in line[counter+1]):
                    print("##############################################")
                    print("C-C-C-C-C-COOOOOOOOOOOMMMMMBBBBOOOOO BREAKER")
                    counter = -1
            datasheet = DataSheet(course_list)
            student_lst.append(
                Student(line[0], "NA", datasheet, line[counter]))
    return student_lst


def is_none(string):
    if string != "None":
        return int(string)
    else:
        return None


def plot_student_grade_avg():
    students = read_from_csv("./students.csv")
    students.sort(key=lambda x: x.get_grades_avg(), reverse=True)

    for sdt in students:
        print("###################################################")
        print(sdt.name)
        print(sdt.image_url)
        print(sdt.get_grades_avg())

    sdt_names = []
    sdt_avg = []

    for i in range(0, len(students)):
        sdt_names.append(students[i].name + "#" + str(i))
        sdt_avg.append(students[i].get_grades_avg())

    plt.bar(sdt_names, sdt_avg, width=0.5, align='center')
    title = 'Student grades average'
    plt.title(title, fontsize=12)
    plt.xlabel("Name", fontsize=10)
    plt.ylabel("Average", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.show()


def plot_student_etcs_progress():
    students = read_from_csv("./students.csv")
    students.sort(key=lambda x: x.get_etcs_progress(), reverse=True)

    for sdt in students:
        print("###################################################")
        print(sdt.name)
        print(sdt.image_url)
        print(sdt.get_etcs_progress())

    sdt_names = []
    sdt_prg = []

    for i in range(0, len(students)):
        sdt_names.append(students[i].name + "#" + str(i))
        sdt_prg.append(students[i].get_etcs_progress())

    plt.bar(sdt_names, sdt_prg, width=0.5, align='center')
    title = 'Student ETCS progress'
    plt.title(title, fontsize=12)
    plt.xlabel("Name", fontsize=10)
    plt.ylabel("%", fontsize=10)
    plt.ylim(0, 100)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.show()


students = create_students(5)
write_to_csv("./students.csv", students)
# plot_student_grade_avg()
plot_student_etcs_progress()
