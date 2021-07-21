from django import forms
from .models import Task

titleclass = "w-full border border-grey-300 px-3 py-2 bg-white rounded-lg shadow-sm focus:outline-none focus:border-blue-300 focus:ring-2 focus:ring-blue-300"

textfieldclass = "w-full border border-grey-300 px-3 py-2 rounded-lg shadow-sm focus:outline-none focus:border-blue-300 focus:ring-2 focus:ring-blue-300"


class TaskForm(forms.ModelForm):

   
    

    class Meta:
        model = Task
        fields = ("__all__")
        ordering = ["created"]
        widgets = {
            'title':forms.TextInput(attrs={"placeholder": "Add a new task", "class": titleclass}),
            'description':forms.Textarea(attrs={"placeholder": "Add a description", "class": textfieldclass}),
            'complete':forms.CheckboxInput(attrs={"class":"rounded-full border-grey-300 text-pink-500 focus:border-blue-400 focus:ring-blue-600"}),
            'due_date':forms.TextInput(attrs={"placeholder": "Add the due date", "class": titleclass, "type":"date", "required":"required"}),
            'priority': forms.Select(attrs={'class':titleclass, "required":"required"}),
        }
