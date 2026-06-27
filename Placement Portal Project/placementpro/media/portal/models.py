from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    package = models.CharField(max_length=50, default="N/A")

    def __str__(self):
        return self.name


class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="Applied")

    def __str__(self):
        return f"{self.student.name} - {self.company.name}"