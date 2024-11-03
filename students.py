class Student:
    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def total_marks(self):
        return sum(self.marks.values())

    def percentage(self, max_mark_per_subject):
        total_possible_marks = max_mark_per_subject * len(self.marks)
        return (self.total_marks() / total_possible_marks) * 100 if total_possible_marks > 0 else 0

student = Student("Іван")

student.add_mark("Математика", 85)
student.add_mark("Фізика", 90)
student.add_mark("Історія", 78)

print(student.total_marks())

print(student.percentage(100))

