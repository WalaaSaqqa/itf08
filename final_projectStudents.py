from datetime import datetime
import random


my_name = "Walaa Sadi Al Saqqa"
Engineer = "Eng. Mohanad AlKrunz"
current_date = datetime.now().date()

print(my_name, "\t\t\t", Engineer, "\t\t\t", "Current Date:", current_date)
print("\n")
class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = random.randint(1000, 9999)
        self.course_name = course_name
        self.course_mark = course_mark


class Student:
    total_students_count = 0

    def __init__(self, student_name, student_age, student_number):
        self.student_id = random.randint(1000, 9999)
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []

    def enroll_new_course(self):
        student_no = input("Enter student number: ")
        for student in student_list:
            if student_number == student_no:
                course_name = input("Enter course name: ")
                course_mark = int(input("Enter the mark for the course: "))
                course = Course(course_name, course_mark)
                student.courses_list.append(course)
                with open("student_Info.txt", "a") as file:
                    file.write("course name: " + course_name + "\n")
                    file.write("course mark: " + str(course_mark) + "\n")
                print("course added successfully. Thank You..")

            else:
                print("student is not exist")

    def get_student_details(self):
        for course in self.courses_list:
            print(f"Course: {course.course_name}, Mark: {course.course_mark}")

    def get_student_average(self):
        if not self.courses_list:
            return 0.0
        total_mark = sum(course.course_mark for course in self.courses_list)
        return total_mark / len(self.courses_list)

    students_list = []

    def exit_program(self):
        print("Exiting program.")
        exit()

    def get_student(self):
        stu  = {
            "student_id": self.student_id,
            "student_name": self.student_name,
            "student_age": self.student_age,
            "student_number": self.student_number,
            "Course Name :": [course.course_name for course in self.courses_list],
            "Course Mark ": [course.course_mark for course in self.courses_list]

                    }
        return stu

student_list = []

while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student details\n"
                              "4.Add a course and mark\n"
                              "5.Get Student Average\n"
                              "6.Exit\n"))


        if selection == 1:
            student_number = input("Enter Student Number: ")
            student_name = input("Enter Student Name: ")
            student_age = input("Enter Student Age: ")

            with open("student_Info.txt", "a") as file:
                file.write("student number: " + student_number + "\n")
                file.write("student name: " + student_name + "\n")
                file.write("student age: " + student_age + "\n")

            new_student = Student(student_name, student_age, student_number)
            student_list.append(new_student)
            print("\nStudent Added Successfully\n")

        elif selection == 2:
            student_number = input("Enter Student Number: ")
            found = False
            for student in student_list:
                if student.student_number == student_number:
                    student_list.remove(student)
                    print("\nStudent Deleted Successfully\n")
                    found = True
                    break
            if not found:
                print("\nStudent Not Exist\n")

        elif selection == 3:
            student_number = input("Enter Student Number: ")
            for student in student_list:
                if student.student_number == student_number:
                    print(student.get_student())


                    break
            else:
                print("\nStudent Not Exist\n")



        elif selection == 4:
            # student_number = input("Enter Student Number: ")
            for student in student_list:
                if student.student_number == student_number:
                    student.enroll_new_course()
                else:
                    print("Student Not Exist")

        elif selection == 5:
            student_number = input("Enter Student Number: ")
            found = 0
            for student in student_list:
                if student.student_number == student_number:
                    found = student
                    break

            if found:
                average = found.get_student_average()
                print(f"Student Average: {average}")

            else:
                print("Student Not Exist")

        elif selection == 6:
            print("\nExiting the program.\n")
            exit()

        else:
            print("\nInvalid selection. Please choose a valid option.\n")

    except ValueError:
        print("Invalid input. Please enter a number.")
