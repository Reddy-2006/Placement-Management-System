from django.shortcuts import render, redirect
from .models import Student, Company, Application


def get_student(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return None
    return Student.objects.filter(id=student_id).first()


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        student = Student.objects.filter(email=email, password=password).first()

        if student:
            request.session['student_id'] = student.id
            return redirect('/dashboard/')

    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        return redirect('/login/')

    return render(request, 'register.html')


def dashboard(request):
    student = get_student(request)
    if not student:
        return redirect('/login/')

    return render(request, 'dashboard.html', {
        'companies': Company.objects.all(),
        'companies_count': Company.objects.count(),
        'applications_count': Application.objects.count()
    })


def companies(request):
    return render(request, 'companies.html', {
        'companies': Company.objects.all()
    })


def apply_form(request, id):
    student = get_student(request)
    if not student:
        return redirect('/login/')

    company = Company.objects.get(id=id)

    if request.method == "POST":
        Application.objects.create(student=student, company=company)
        return redirect('/applications/')

    return render(request, 'apply_form.html', {'company': company})


def applications(request):
    student = get_student(request)
    if not student:
        return redirect('/login/')

    return render(request, 'applications.html', {
        'applications': Application.objects.filter(student=student)
    })