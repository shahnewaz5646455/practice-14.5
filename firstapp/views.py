from django.shortcuts import render
from . forms import contactForm
from . forms2 import ModelForm
# Create your views here.
def django_form(request):
    form = contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'django_form.html', {'form':form})



def model(request):
    
    model_form = ModelForm
    return render(request, 'model_form.html', {'form' : model_form})