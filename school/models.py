from django.db import models

class HOD(models.Model):
    hod_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)


class Student(models.Model):
    roll_no = models.CharField(max_length=20, primary_key=True)  # Use roll_no as PK
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=50)


class Subject(models.Model):
    code = models.CharField(max_length=10, primary_key=True)  # Use subject code as PK
    subject_name = models.CharField(max_length=30)



class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

class Mark(models.Model):
    mark_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    exam_name = models.CharField(max_length=50)  # e.g., Midterm, Final