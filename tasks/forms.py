from django import forms
from tasks.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task

        fields = ['title','description','due_date']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'rows':1}),
            'due_date':forms.DateTimeInput(attrs={'class':'form-control', 'type':'datetime-local'})

        }
