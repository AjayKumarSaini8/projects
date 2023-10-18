from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Teacher, Student, Certificate, TeacherStudentPair
from .forms import PairSelectionForm

def landing_page(request):
    return render(request, 'landing_page.html')

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher_list.html'
    context_object_name = 'teachers'

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

def students_for_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    students = teacher.students.all()
    return render(request, 'students_for_teacher.html', {'teacher': teacher, 'students': students})

def teachers_for_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    teachers = student.teachers.all()
    return render(request, 'teachers_for_student.html', {'student': student, 'teachers': teachers})

def create_certificate(request):
    if request.method == 'POST':
        form = PairSelectionForm(request.POST)
        if form.is_valid():
            teacher_student_pair = form.cleaned_data['teacher_student_pair']
            student_name = teacher_student_pair.student.name
            title = "Certificate Title"  # You can customize the title as needed
            date = "2023-10-17"  # Use the actual date or customize it

            # Create the Certificate object
            certificate = Certificate.objects.create(
                student_name=student_name,
                title=title,
                date=date,
                teacher_student_pair=teacher_student_pair
            )

            return redirect('certificate_created')  # Redirect to a success page
    else:
        form = PairSelectionForm()

    return render(request, 'select_pair.html', {'form': form})

def select_pair(request):
    if request.method == 'POST':
        form = PairSelectionForm(request.POST)
        if form.is_valid():
            teacher_student_pair = form.cleaned_data['teacher_student_pair']
            student_name = teacher_student_pair.student.name
            title = "Certificate Title"  # You can customize the title as needed
            date = "2023-10-17"  # Use the actual date or customize it

            # Create the Certificate object
            certificate = Certificate.objects.create(
                student_name=student_name,
                title=title,
                date=date,
                teacher_student_pair=teacher_student_pair
            )

            return redirect('certificate_created')  # Redirect to a success page
    else:
        form = PairSelectionForm()

        # Get all available teacher-student pairs
        teacher_student_pairs = TeacherStudentPair.objects.all()

    return render(request, 'select_pair.html', {'form': form, 'teacher_student_pairs': teacher_student_pairs})

def certificate_created(request):
    return render(request, 'certificate_created.html')