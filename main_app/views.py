# main_app/views.py
from django.shortcuts import redirect, render
from .models import Dog
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import the FeedingForm
from .forms import FeedingForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
# Other imports above
from django.views.generic import ListView, DetailView
# Add the two imports below
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin


# Define the home view function
class Home(LoginView):
    template_name = 'home.html'

# def home(request):
#     return render(request, 'home.html')


def home(request):
    form = AuthenticationForm()
    return render(request, 'home.html', {'form': form})


def about(request):
    # return HttpResponse('<h1>About the DogCollector</h1>')
    return render(request, 'about.html')

@login_required
def dog_index(request):
    # Render the dogs/index.html template with the dogs data
    # dogs = Dog.objects.all()
    dogs = Dog.objects.filter(user=request.user)
    # You could also retrieve the logged in user's dogs like this
    # dogs = request.user.dog_set.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})

@login_required
def dog_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'dogs/detail.html', {
        # include the dog and feeding_form in the context
        'dog': dog, 'feeding_form': feeding_form
    })

LoginRequiredMixin,
class DogCreate(CreateView):
    model = Dog
    # fields = '__all__'
    fields = ['name', 'breed', 'description', 'age']
    # success_url = '/dogs/'

LoginRequiredMixin,
class DogUpdate(UpdateView):
    model = Dog
    # Let's disallow the renaming of a dog by excluding the name field!
    fields = ['breed', 'description', 'age']

LoginRequiredMixin,
class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'

@login_required
def add_feeding(request, dog_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the dog_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.dog_id = dog_id
        new_feeding.save()
    return redirect('dog-detail', dog_id=dog_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('dog-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )



#TODO: left at Integrating MCDatepicker for a custom date picker
#TODO: Create a Update the DogCreate view to assign a new dog to the logged in user
#TODO: Implement full CRUD operations for the secondary model, ensuring resources can be created, read, updated, and deleted.
#TODO: Create a one-to-many data relationship in Django : Dogs -< Feedings





