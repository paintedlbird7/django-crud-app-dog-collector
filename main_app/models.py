from django.db import models
from django.urls import reverse
# Import the User
from django.contrib.auth.models import User

# A tuple of 2-tuples added above our models
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
       # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

     # Define a method to get the URL for this particular dog instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this dog's details
        return reverse('dog-detail', kwargs={'dog_id': self.id})
    # This inherited method is called when a
    # valid dog form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the dog
        # Let the CreateView do its job as usual
        return super().form_valid(form)
    
    # Add new Feeding model below Dog model
class Feeding(models.Model):
    date = models.DateField('Feeding date')
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0]
    )
      # Create a dog_id column for each feeding in the database
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"
      # Define the default order of feedings
    class Meta:
        ordering = ['-date']  # This line makes the newest feedings appear first

