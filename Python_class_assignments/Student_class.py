class Student:
    
    all_students = []

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student.all_students.append(self)
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, new_grade):
        if new_grade < 0 or new_grade > 100:
            raise ValueError("New grade not in the accepted range of [0 - 100].")
        self._grade = new_grade

    @classmethod
    def get_average_grade(cls):
        return cls.calculate_average_grade(cls.all_students)
    
    @classmethod
    def get_best_student(cls):
        if len(cls.all_students) == 0: 
            return None
        
        highest_grade = 0

        for item in cls.all_students:
            temp_highest_grade = item.grade
            if temp_highest_grade > highest_grade:
                best_student = item
                highest_grade = temp_highest_grade

        return best_student

    @staticmethod
    def calculate_average_grade(students):
        
        if len(students) == 0:
            return -1

        sum_grade = 0
        for item in students:
            sum_grade += item.grade
        return sum_grade / len(students)

