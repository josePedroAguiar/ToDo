from  django.forms import ModelForm
from .models import ToDo as todo

class ToDoForm(ModelForm):
    class Meta:
        model=todo
        fields=['title','note','important','deadline', ]
