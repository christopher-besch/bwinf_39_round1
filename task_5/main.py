import re


class Student:
    """
    representing a single student with references to their wished packages
    """
    def __init__(self, number, wishes):
        self.number = number
        # tuple with one package number per wish (1st wish, 2nd wish...)
        self.wishes = wishes

    def __repr__(self):
        return f"id: {self.number}; wishes: {self.wishes}"


class Package:
    """
    representing a single package with references to all the students wanting this package
    """
    def __init__(self, number, wishers):
        self.number = number
        # tuple with one list per wish (1st wish, 2nd wish...) with all the students (wishers) wanting this package
        self.wishers = wishers

    def __repr__(self):
        return f"id: {self.number}; wishers: {self.wishers}"


class Selection:
    """
    containing all the students and packages
    methods can assign students to packages in three different ways:
        1. assign_all_cleanly:
            try to assign packages that are only wanted by a single student
            -> no package gets taken away from a different student wanting it the same way or more
        2. assign_all_uncleanly:
            assign students to packages with taking packages away from students wanting it the same way
            leaving only completely unwanted packages
        3. assign_all_dirtily:
            assign packages to students, including completely unwanted packages
            no packages or student stays unassigned
    """
    def __init__(self, students, packages):
        if len(students) != len(packages):
            raise ValueError("The amount of students doesn't match the amount of packages!")
        # key: student number, value: Student instance
        self.students = students
        # key: package number, value: Package instance
        self.packages = packages
        # key: package number, value: student number
        self.assigned_students = {}
        self.amount_wishes = len(self.students[1].wishes)

    def __repr__(self):
        return f"{len(self.students)} students with {self.amount_wishes} wishes each; " \
               f"{len(self.assigned_students)} students already have a package assigned to them"

    def get_unassigned_wishers(self, package_number, wish_id):
        """
        get all the students wanting this package (according to wish_id) that aren't assigned yet
        """
        # get Package object
        package = self.packages[package_number]
        # get all students having this package as their wish (according to wish_id) that aren't assigned
        return [wisher for wisher in package.wishers[wish_id] if wisher not in self.assigned_students.keys()]

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
        see if this package is only wanted by one student (according to wish_id)
        and then assign it

        return True when this is a package wanted by multiple students, else False
        """
        # get unassigned wishers
        unassigned_wishers = self.get_unassigned_wishers(package_number, wish_id)
        # when only a single student wants this package, they get it
        if len(unassigned_wishers) == 1:
            this_student_number = unassigned_wishers[0]
            # assign this student to the wanted package if they aren't assigned yet
            if this_student_number not in self.assigned_students.keys():
                self.assign(this_student_number, package_number)

                # see if that assignment resolved a problem with a more important wish
                # <- one student less to find a package for
                self.resolve_after_assignment(this_student_number, wish_id - 1)
        # when this package is wanted by multiple students
        elif len(self.packages[package_number].wishers[wish_id]) > 1:
            return True
        return False

    def resolve_after_assignment(self, student_number, wish_id):
        """
        recursive function (calling itself and assign_package_if_possible)
        see if an assignment (student_number got assigned) resolved a problem with a more important wish (wish_id)
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
        self.resolve_after_assignment(student_number, wish_id - 1)

    def assign_packages(self, wish_id, disallowed_packages):
        """
        (cleanly) assign all packages that are wanted by only one student (according to wish_id)
        and check if that assignment solved a problem with a more important wish

        return all the packages that are wanted by multiple students
        """
        # numbers of all packages wanted by multiple students
        highly_wanted_package = []
        for package_number in self.packages.keys():
            # don't try to assign this package if it is disallowed or already assigned
            if package_number not in disallowed_packages and package_number not in self.assigned_students.values():
                # assign if possible
                is_highly_wanted = self.assign_package_if_possible(package_number, wish_id)
                # add this package if it is highly wanted
                if is_highly_wanted:
                    highly_wanted_package.append(package_number)
        return highly_wanted_package

    def assign_all_cleanly(self):
        """
        try to assign packages that are only wanted by a single student
        -> no package gets taken away from a different student wanting it the same way or more
        """
        # these packages are wanted so much that less relevant wishes can't be used to assign it
        highly_wanted_packages = []
        for wish_id in range(self.amount_wishes):
            # assign everything possible for this wish_id
            # and try to resolve as many problems in more important wishes as possible
            highly_wanted_packages += self.assign_packages(wish_id, highly_wanted_packages)

    def assign_all_uncleanly(self):
        """
        go through all wishes and just assign the first student with their wished package
        -> other students wanting this package in the same way won't get it
        """
        # go through all unassigned students
        for wish_id in range(self.amount_wishes):
            for student_number in self.students.keys():
                if student_number in self.assigned_students.keys():
                    # this student is already assigned
                    continue
                wished_package = self.students[student_number].wishes[wish_id]
                # just assign it if the package is not assigned yet
                if wished_package not in self.assigned_students.values():
                    self.assign(student_number, wished_package)

    def assign_all_dirtily(self):
        """
        go through all unassigned students and unassigned packages and just assign with no regard to their wishes
        should only be used when there are only unwanted packages left to be assigned
        """
        # get all unassigned packages
        unassigned_package_numbers = [package_number for package_number in self.packages.keys()
                                      if package_number not in self.assigned_students.values()]
        for wish_id in range(self.amount_wishes):
            for student_number in self.students.keys():
                if student_number not in self.assigned_students.keys():
                    # just take and delete the last unassigned package number and assign it
                    self.assign(student_number, unassigned_package_numbers.pop())


def load_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file]
        # the first line only contains the amount of students, which won't be used
        return lines[1:]


def load_students_and_packages(lines):
    """
    get lines read from the file and create a Selection object
    """
    # get the amount of wishes every student has
    wishes_amount = len(re.split(r"[\W]+", lines[0]))
    # key: package number, value: Package instance
    # fill it with no student wanting any packages
    packages = {number: Package(number, tuple([] for _ in range(wishes_amount))) for number in range(1, len(lines) + 1)}

    # key: student number, value: Student instance
    students = {}
    for student_idx, line in enumerate(lines):
        """
        fill students
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
    # load students and packages form file
    lines = load_file("beispieldaten/my_wichteln2.txt")
    selection = load_students_and_packages(lines)

    # assign all packages and students
    selection.assign_all_cleanly()
    selection.assign_all_uncleanly()
    selection.assign_all_dirtily()

    # print results
    print("student number, [wishes], assigned package")
    for student_number in selection.students:
        # convert this student's wishes into a usable string
        wishes = [str(wish) for wish in selection.students[student_number].wishes]
        wishes_string = "\t".join(wishes)
        # get the package that got assigned to this student
        assigned_package = selection.assigned_students[student_number]

        print(f"{student_number}\t\t{wishes_string}\t\t{assigned_package}")


if __name__ == "__main__":
    main()
