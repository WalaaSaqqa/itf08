def main():
    num_stud = int(input("Enter the number of students: "))

    for stud in range(1, num_stud + 1):
        num_marks = int(input(f"Enter the number of marks for student {stud}: "))

        marks = []
        for mark_num in range(1, num_marks + 1):
            mark = float(input(f"Enter mark {mark_num} for student {stud}: "))
            marks.append(mark)

        average_mark = sum(marks) / num_marks
        average_mark = round(average_mark, 2)
        max_mark = max(marks)
        min_mark = min(marks)

        print(f"Student {stud} :\n "
              f"    Average: {average_mark},     Max: {max_mark},      Min: {min_mark}")



main()
