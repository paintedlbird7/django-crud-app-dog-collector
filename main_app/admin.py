from django.contrib import admin
# Add Feeding to the import
from .models import Dog, Feeding

admin.site.register(Dog)
# Register the new Feeding model
admin.site.register(Feeding)
