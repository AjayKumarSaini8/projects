from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=15)
    teachers = models.ManyToManyField('Teacher', related_name='students', blank=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=15)
    

    def __str__(self):
        return self.name
    
class Certificate(models.Model):
    student_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date = models.DateField()
    teacher_student_pair = models.ForeignKey(
        'home.TeacherStudentPair',  # Use the string representation of the model
        on_delete=models.CASCADE,
        related_name='certificates'
    )

    def __str__(self):
        return f"Certificate for {self.student_name} - {self.title}"

class TeacherStudentPair(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.teacher.name} - {self.student.name}"
