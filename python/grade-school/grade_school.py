class School:
    def __init__(self):
        self.enrolled = []

    def add_student(self, name, grade):
        """ add a student to school """

        self.enrolled.append({"name": name, "grade": grade})

    def roster(self):
        """ list the roster of students """

        ret = []

        self.enrolled.sort(key=lambda x: x.get("name"))
        self.enrolled.sort(key=lambda x: x.get("grade"))

        for student in self.enrolled:
            ret.append(student.get("name", None))
        return ret

    def grade(self, grade_number):
        """ list the students by grade """

        ret = []

        self.enrolled.sort(key=lambda x: x.get("name"))
        self.enrolled.sort(key=lambda x: x.get("grade"))

        for student in self.enrolled:
            if student.get("grade") == grade_number:
                ret.append(student.get("name", None))

        return ret
