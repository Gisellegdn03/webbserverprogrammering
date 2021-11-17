from django.shortcuts import render
from django.http.response import HttpResponse
from django.forms.forms import Form
from django import forms


tasklist = ["study", "Engineer gaming", "do the dishes", "cook", "clean my room" ]
class NewTaskForm (forms.Form):
    task = forms.CharField(label="Add task")

# Create your views here.
def home(request):
    return render(request, "tasklist.html")

def add(request):
    if request.method=="POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            tasklist.append(task)
            return render(request, 'tasklist.html', {
                'tasklist':tasklist,
                'form':form
            })
        else:
            return render(request, 'tasklist.html', {
                "form":form
            })
    return render(request, 'tasklist.html',{
        "form":NewTaskForm(),
        "tasklist":tasklist
    })