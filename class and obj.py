'''class student:
    def __init__(self,name,rollno,maths,python,java,social,science):
        self.name=name
        self.rollno=rollno
        self.maths=maths
        self.python=python
        self.java=java
        self.social=social
        self.science=science
obj=student("sravya",22,56,72,88,69,90)
print(obj.name)
print(obj.rollno)
print(obj.maths)
print(obj.python)
print(obj.java)
print(obj.social)
print(obj.science)
obj1=student("jhansi",77,98,67,32,55,99)
print(obj1.name)
print(obj1.rollno)
print(obj1.maths)
print(obj1.python)
print(obj1.java)
print(obj1.social)
print(obj1.science)
obj2=student("pooja",33,43,59,86,51,97)
print(obj2.name)
print(obj2.rollno)
print(obj2.maths)
print(obj2.python)
print(obj2.java)
print(obj2.social)
print(obj2.science)'''


class student:
    def __init__(self,name,rollno,maths,python,java,social,science):
        self.name=name
        self.rollno=rollno
        self.maths=maths
        self.python=python
        self.java=java
        self.social=social
        self.science=science
    def member(self):
        print(self.name)
        print(self.rollno)
        print(self.maths)
        print(self.python)
        print(self.java)
        print(self.social)
        print(self.science)
obj=student("sravya",22,56,72,88,69,90)
obj.member()
obj1=student("jhansi",77,98,67,32,55,99)
obj1.member()
obj2=student("pooja",33,43,59,86,51,97)
obj2.member()


