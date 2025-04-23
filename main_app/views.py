# main_app/views.py
from django.shortcuts import render
from .models import Dog
from django.views.generic.edit import CreateView



# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('<h1>About the DogCollector</h1>')
    return render(request, 'about.html')


def dog_index(request):
    # Render the dogs/index.html template with the dogs data
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})

def dog_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/detail.html', {'dog': dog})

class DogCreate(CreateView):
    model = Dog
    # fields = '__all__'
    fields = ['name', 'breed', 'description', 'age']
    success_url = '/dogs/'


#TODO: Create the template for creating cats



