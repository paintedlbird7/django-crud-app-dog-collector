# main_app/views.py
from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    # return HttpResponse('<h1>About the DogCollector</h1>')
    return render(request, 'about.html')

class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

# Create a list of Cat instances
dogs = [
    Dog('Lolo', 'tabby', 'Kinda rude.', 3),
    Dog('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
    Dog('Fancy', 'bombay', 'Happy fluff ball.', 4),
    Dog('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

# views.py

def dog_index(request):
    # Render the dogs/index.html template with the dogs data
    return render(request, 'dogs/index.html', {'dogs': dogs})

#TODO: 🎓Left off at You Do: Create a template for the home page
