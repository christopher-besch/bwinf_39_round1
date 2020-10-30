import re


class Student:
    def __init__(self, number, wishes):
        self.number = number
        # tuple with one package number per wish (1st wish, 2nd wish...)
        self.wishes = wishes

    def __repr__(self):
        return f"id: {self.number}; wishes: {self.wishes}"


class Package:
    def __init__(self, number, students):
        self.number = number
        # tuple with one list per wish (1st wish, 2nd wish...) with all the students wanting this package
        self.students = students

    def __repr__(self):
        return f"id: {self.number}; students: {self.students}"


def load_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file]
        return lines[1:]


def load_students_and_packages(lines):
    # get the amount of wishes every student has
    wishes_amount = len(re.split(r"[\W]+", lines[0]))
    # dict with package number as key and Package instance as value
    packages = {number: Package(number, ([],) * wishes_amount) for number in range(1, len(lines) + 1)}

    # dict with student number as key and Student instance as value
    students = {}
    # when the line doesn't contain any wishes the loop doesn't continue
    for student_idx, line in enumerate(lines):
        # split line into words
        wishes = tuple(int(package_number) for package_number in re.split(r"[\W]+", line))
        # create Student instance and add to dict
        student = Student(student_idx + 1, wishes)
        students[student.number] = student
        # go through every wished package
        for wish_idx, package_number in enumerate(student.wishes):
            # append Student instance to the the wished-by-list
            packages[package_number].students[wish_idx].append(student.number)
    return students, packages


def main():
    lines = load_file("beispieldaten/wichteln1.txt")
    students, packages = load_students_and_packages(lines)
    pass


if __name__ == "__main__":
    main()
