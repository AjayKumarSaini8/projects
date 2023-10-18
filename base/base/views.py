from django.shortcuts import render, redirect
from home.models import TeacherStudentPair, Certificate
from home.forms import PairSelectionForm

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

# Other views here
