#Practical-9
'''
Consider an example of declaring the examination result.
Design three classes: Student, Exam, and Result. The Student class has data members such
as those representing rollNumber, Name, etc.
Create the class Exam by inheriting Student class. The Exam class adds fields representing the marks scored in six subjects.
Derive Result from the Exam class, and it has its own fields such as total_marks.
Write an interactive program to model this relationship.
'''


class Student(object):
    rollNo = input("Enter the roll number: ")
    print(rollNo)
    name = input("Enter the name of the student: ")
    print(name)


class Exam(Student):
    def exam(self, s1, s2, s3, s4, s5, s6):
        total = s1 + s2 + s3 + s4 + s5 + s6
        print("Total marks: ",total)


class Result(Exam):
    Exam.exam(1, 10, 20, 30, 40, 50, 60)


s = Student()
e = Exam()
r = Result()

