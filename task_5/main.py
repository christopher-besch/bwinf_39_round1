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
        # key: package number, value: student number
        self.assigned_students = {}
        self.amount_wishes = len(self.students[1].wishes)

    def __repr__(self):
        return f"{len(self.students)} wishers with {self.amount_wishes} wishes each; " \
               f"{len(self.assigned_students)} wishers already have a package assigned to them"

    def assign(self, student_number, package_number):
        """
        assign student to package
        """
        if student_number in self.assigned_students.keys() or package_number in self.assigned_students.values():
            raise ValueError("Trying to assign an already assigned student or an already assigned package!")
        self.assigned_students[student_number] = package_number

    def assign_package_if_possible(self, package_number, wish_id):
        """
        recursive function (calling resolve_after_assignment)
        see if this package is only wanted by one person (according to wish_id)
        and then assign it
        """
        # get package
        package = self.packages[package_number]
        # when only a single student wants this package, they get it
        if len(package.wishers[wish_id]) == 1:
            this_student_number = package.wishers[wish_id][0]
            # assign this student to the wanted package if they aren't assigned yet
            if this_student_number not in self.assigned_students.keys():
                self.assign(this_student_number, package_number)

                # see if that assignment resolved a problem with a more important wish
                # <- one student less to find a package again
                self.resolve_after_assignment(this_student_number, wish_id - 1)
        # when this package is wanted by multiple people
        elif len(package.wishers[wish_id]) > 1:
            return True
        return False

    # todo: check
    def resolve_after_assignment(self, student_number, wish_id):
        """
        recursive function (calling assign_package_if_possible)
        see if that assignment resolved a problem with a more important wish
        go through all more important wishes than the current one
        """
        # when this wish doesn't exists
        if wish_id < 0:
            return

        # now this package has one student less wanting it
        package_number = self.students[student_number].wishes[wish_id]
        # when this package is not assigned yet
        if package_number not in self.assigned_students.values():
            # see if it can be assigned -> resolve even more problems if possible
            self.assign_package_if_possible(package_number, wish_id)
        # do the same with the next more important wish
        self.resolve_after_assignment(package_number, wish_id - 1)

    def assign_packages(self, wish_id, disallowed_packages):
        """
        assign all packages that are wanted by only one student (according to wish_id)
        and check if that assignment solved a problem with a more important wish
        """
        # numbers of all packages wanted by multiple students
        highly_wanted_package = []
        for package in self.packages.values():
            # don't try to assign this package if it is disallowed or already assigned
            if package.number in disallowed_packages or package.number in self.assigned_students.values():
                continue
            # assign if possible
            wanted_by_multiple = self.assign_package_if_possible(package.number, wish_id)
            if wanted_by_multiple:
                highly_wanted_package.append(package.number)
        return highly_wanted_package

    def assign_all(self):
        """
        try to assign all packages
        """
        # these packages are wanted so much that less relevant wishes can't be used to assign it
        highly_wanted_packages = []
        for wish_id in range(self.amount_wishes):
            # assign everything possible for this wish_id
            # and try to resolve as many problems in more important wishes as possible
            highly_wanted_packages += self.assign_packages(wish_id, highly_wanted_packages)


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


def main():
    lines = load_file("beispieldaten/wichteln7.txt")
    selection = load_students_and_packages(lines)
    selection.assign_all()
    print(selection)


if __name__ == "__main__":
    main()
