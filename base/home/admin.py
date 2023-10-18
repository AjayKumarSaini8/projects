from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms
from .models import Student, Teacher

# Custom Form for Student Model
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'mobile_no', 'teachers']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teachers'].widget = FilteredSelectMultiple('Teachers', is_stacked=False)
        self.fields['teachers'].queryset = Teacher.objects.all()

# Register the Student Model with the Custom Form
class StudentAdmin(admin.ModelAdmin):
    form = StudentForm

admin.site.register(Student, StudentAdmin)

# Register the Teacher Model
admin.site.register(Teacher)
