# main_app/views.py
from django.shortcuts import render
from .models import Dog
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



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
    # success_url = '/dogs/'

class DogUpdate(UpdateView):
    model = Dog
    # Let's disallow the renaming of a dog by excluding the name field!
    fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'


#TODO: left at Updating & deleting dogs with class-based views
#TODO: Create a one-to-many relationship with a second model.
#TODO: Implement full CRUD operations for the secondary model, ensuring resources can be created, read, updated, and deleted.
#TODO: Create a one-to-many data relationship in Django : Dogs -< Feedings





