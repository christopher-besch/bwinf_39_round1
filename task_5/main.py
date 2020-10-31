import re


class Student:
    def __init__(self, number, wishes):
        self.number = number
        # tuple with one package number per wish (1st wish, 2nd wish...)
        self.wishes = wishes

    def __repr__(self):
        return f"id: {self.number}; wishes: {self.wishes}"


class Package:
    def __init__(self, number, wishers):
        self.number = number
        # tuple with one list per wish (1st wish, 2nd wish...) with all the students wanting this package
        self.students = wishers

    def __repr__(self):
        return f"id: {self.number}; students: {self.students}"


class Selection:
    def __init__(self, students, packages):
        # key: student number, value: Student instance
        self.students = students
        # key: package number, value: Package instance
        self.packages = packages
        # key: package number, value: student number
        self.assigned_packages = {}

    def __repr__(self):
        amount_wishes = len(self.students[1].wishes)
        return f"{len(self.students)} students with {amount_wishes} wishes each; " \
               f"{len(self.assigned_packages)} students already have a package assigned to them"

    # assign student to package
    def assign(self, package_number, student_number):
        if package_number in self.assigned_packages.keys() or student_number in self.assigned_packages.values():
            raise ValueError("Trying to assign an already assigned student or an already assigned package!")
        self.assigned_packages[package_number] = student_number


def load_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file]
        # the first line only contains the amount of students, which won't be used
        return lines[1:]


def load_students_and_packages(lines):
    # get the amount of wishes every student has
    wishes_amount = len(re.split(r"[\W]+", lines[0]))
    # key: package number, value: Package instance
    # fill it with no students wanting any packages
    packages = {number: Package(number, tuple([] for _ in range(wishes_amount))) for number in range(1, len(lines) + 1)}

    # key: student number, value: Student instance
    students = {}
    for student_idx, line in enumerate(lines):
        # split line into words
        wishes = tuple(int(package_number) for package_number in re.split(r"[\W]+", line))
        # create Student instance and add to dict
        student = Student(student_idx + 1, wishes)
        students[student.number] = student
        # go through every wished package
        for wish_idx, package_number in enumerate(student.wishes):
            # append student number to the wished-by-list
            packages[package_number].students[wish_idx].append(student.number)
    return students, packages


def assign_packages(selection, wish_id, disallowed_packages):
    for package in selection.packages.values():
        # don't try to assign this package if it is disallowed or already assigned
        if package.number in disallowed_packages or package.number in selection.assigned_packages:
            continue
        # when only a single student wants this package, they get it
        if len(package.students[wish_id]) == 1:
            # assign wanted package to this user
            selection.assign(package.number, selection.students[wish_id][0])
            # see if that assignment resolved a problem with a more important wish
            resolve_after_assignment(selection, package.number, wish_id)


def resolve_after_assignment(selection, package_number, highest_wish_id):
    """
    recursive function
    see if that assignment resolved a problem with a more important wish
    """
    # go through all more important wishes than the current one
    for current_wish_id in reversed(range(highest_wish_id)):
        unassigned_wisher_numbers = get_unassigned_wishers(selection, package_number, current_wish_id - 1)
        if len(unassigned_wisher_numbers) != 1:
            break
        selection.assign(unassigned_wisher_numbers[0], package_number)
        # todo: get wanted packages
        for package in selection.students[unassigned_wisher_numbers[0]].wishes:
            resolve_after_assignment(selection, package.number, highest_wish_id - 1)


def get_unassigned_wishers(selection, package_number, wish_id):
    """
    get every unassigned student having this package as their wish (according to wish_id)
    """
    # get all wishers of this package
    wishers = selection.packages[package_number].wishers[wish_id]
    # get their number and and remove every assigned student
    wisher_numbers = [wisher.number for wisher in wishers if wisher.number not in selection.assigned_packages.values()]
    return wisher_numbers


def main():
    lines = load_file("beispieldaten/wichteln1.txt")
    students, packages = load_students_and_packages(lines)
    selection = Selection(students, packages)
    assign_packages(selection, 0, [])
    print(selection)
    pass


if __name__ == "__main__":
    main()
