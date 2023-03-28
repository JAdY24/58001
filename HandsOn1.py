class Person():
  def __init__(self, student, pre, mid, fin):
    self.student = student
    self.pre = pre
    self.mid = mid
    self.fin = fin

  def Grade(self):
    return (self.pre+self.mid+self.fin)/3

  def display(self):
    print("The grade of", self.student, "Prelim", self.pre, "Midterm", self.mid, "Finals", self.fin, "The average is", self.Grade())

class Student1(Person):
  pass
class Student2(Person):
  pass
class Student3(Person):
  pass

student1 = Student1("Student1", 86, 81, 88)
student1.display()
student2 = Student2("Student2",76, 74, 80)
student2.display()
student3 = Student3("Student3",92, 95, 89)
student3.display()