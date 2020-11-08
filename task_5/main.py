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
        # tuple with one list per wish (1st wish, 2nd wish...) with all the wishers wanting this package
        self.wishers = wishers

    def __repr__(self):
        return f"id: {self.number}; wishers: {self.wishers}"


class Selection:
    def __init__(self, students, packages):
        # key: student number, value: Student instance
        self.students = students
        # key: package number, value: Package instance
        self.packages = packages
        # todo: this is fucked up!
        # key: package number, value: student number
        self.assigned_students = {}

    def __repr__(self):
        amount_wishes = len(self.students[1].wishes)
        return f"{len(self.students)} wishers with {amount_wishes} wishes each; " \
               f"{len(self.assigned_students)} wishers already have a package assigned to them"

    # assign student to package
    def assign(self, package_number, student_number):
        if package_number in self.assigned_students.keys() or student_number in self.assigned_students.values():
            raise ValueError("Trying to assign an already assigned student or an already assigned package!")
        self.assigned_students[package_number] = student_number

    # todo: check
    def get_unassigned_wishers(self, package_number, wish_id):
        """
        get every unassigned student having this package as their wish (according to wish_id)
        """
        # get all wishers of this package
        wishers = self.packages[package_number].wishers[wish_id]
        # get their number and and remove every assigned student
        unassigned_wisher_numbers = [wisher.number for wisher in wishers if
                                    wisher.number not in self.assigned_students.values()]
        return unassigned_wisher_numbers


def load_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file]
        # the first line only contains the amount of wishers, which won't be used
        return lines[1:]


def load_students_and_packages(lines):
    # get the amount of wishes every student has
    wishes_amount = len(re.split(r"[\W]+", lines[0]))
    # key: package number, value: Package instance
    # fill it with no wishers wanting any packages
    packages = {number: Package(number, tuple([] for _ in range(wishes_amount))) for number in range(1, len(lines) + 1)}

    # key: student number, value: Student instance
    students = {}
    for student_idx, line in enumerate(lines):
        """
        fill wishers
        """
        # split line into words
        wishes = tuple(int(package_number) for package_number in re.split(r"[\W]+", line))
        # create Student instance and add to dict
        student = Student(student_idx + 1, wishes)
        students[student.number] = student
        """
        fill packages
        """
        # go through every wished package
        for wish_idx, package_number in enumerate(student.wishes):
            # append student number to the wished-by-list
            packages[package_number].wishers[wish_idx].append(student.number)
    return Selection(students, packages)


def assign_packages(selection, wish_id, disallowed_packages):
    for package in selection.packages.values():
        # don't try to assign this package if it is disallowed or already assigned
        if package.number in disallowed_packages or package.number in selection.assigned_students:
            continue
        # when only a single student wants this package, they get it
        if len(package.wishers[wish_id]) == 1:
            # assign wanted package to this user
            selection.assign(package.number, package.wishers[wish_id][0])

            # see if that assignment resolved a problem with a more important wish
            resolve_after_assignment(selection, package.number, wish_id - 1)


# todo: fix
def resolve_after_assignment(selection, package_number, wish_id):
    """
    recursive function
    see if that assignment resolved a problem with a more important wish
    go through all more important wishes than the current one
    """
    if wish_id == 0:
        return

    unassigned_wisher_numbers = get_unassigned_wishers(selection, package_number, wish_id)
    if len(unassigned_wisher_numbers) != 1:
        break
    selection.assign(unassigned_wisher_numbers[0], package_number)
    # todo: get wanted packages
    for package in selection.wishers[unassigned_wisher_numbers[0]].wishes:
        resolve_after_assignment(selection, package.number, highest_wish_id - 1)


def main():
    lines = load_file("beispieldaten/wichteln1.txt")
    selection = load_students_and_packages(lines)
    assign_packages(selection, 0, [])
    print(selection)
    pass


if __name__ == "__main__":
    main()
