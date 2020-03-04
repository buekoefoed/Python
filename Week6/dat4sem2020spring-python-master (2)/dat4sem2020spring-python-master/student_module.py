class Student():
    def __init__(self, id_no, name, gender, data_sheet=None, image_url=None, no_semesters=5):
        self.id = id_no
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url
        self.no_semesters = no_semesters
    
    def __str__(self):
        return 'Student {id}: {name} has average grade: {avg_grade} and progress: {progress}'.format(
          id=self.id
          ,name=self.name
          ,gender=self.gender
          ,avg_grade=self.get_avg_grade()
          ,progress=self.get_progression())
        
    def __eq__(self, other):
        """The eq() method is used for comparing one object to another. 
        Note that implementing __eq__ will automatically make instances of your class unhashable, 
        which means they can't be stored in sets and dicts"""
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)
    
    def get_avg_grade(self):
        grades = self.data_sheet.get_grades() if not self.data_sheet == None else [0] 
        return sum(grades)/len(grades) if len(grades) else None
    
    def get_progression(self):
        total_ects_achieved = sum([c.ects for c in self.data_sheet.courses if not c.grade == None])
        total_ects_to_complete = self.no_semesters * 30
        return total_ects_achieved/total_ects_to_complete*100
    
        
class DataSheet():
    def __init__(self, courses):
        self.courses = courses
        self.index = 0
    
    def __str__(self):
        return 'No of courses: {number} with grades: {grades}'.format(number=len(self.courses),grades=self.get_grades())
    
    def get_grades(self):
        return [c.grade for c in self.courses if not c.grade==None]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if(self.index < len(courses)):
            c = courses[self.index]
            print('next found c:',c)
            self.index = self.index + 1
            return c
        else:
            raise StopIteration
        
class Course():
    def __init__(self, name, classroom, teacher, ects, grade=None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ects = ects
        self.grade = grade
        
    def __str__(self):
        return 'course: {name} in {cl} by {teacher}. ECTS: {ects} closed with grade: {grade}'.format(name=self.name
                                                                                                    ,cl=self.classroom
                                                                                                    ,teacher=self.teacher
                                                                                                    ,ects=self.ects
                                                                                                    ,grade=self.grade)