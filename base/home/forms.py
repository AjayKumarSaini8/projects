from django import forms
from .models import TeacherStudentPair

class PairSelectionForm(forms.Form):
    teacher_student_pair = forms.ModelChoiceField(
        queryset=TeacherStudentPair.objects.all(),
        label="Select a Teacher-Student Pair",
        empty_label="Select a pair"
    )
