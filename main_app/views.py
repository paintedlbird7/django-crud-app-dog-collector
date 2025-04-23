# main_app/views.py
from django.shortcuts import render
from .models import Dog


# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('<h1>About the DogCollector</h1>')
    return render(request, 'about.html')

# class Dog:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# # Create a list of Dog instances
# dogs = [
#     Dog('Lolo', 'tabby', 'Kinda rude.', 3),
#     Dog('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#     Dog('Fancy', 'bombay', 'Happy fluff ball.', 4),
#     Dog('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]

def dog_index(request):
    # Render the dogs/index.html template with the dogs data
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})

def dog_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/detail.html', {'dog': dog})
