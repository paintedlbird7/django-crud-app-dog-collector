from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # Routes will be added here
    # path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for dogs index
    path('dogs/', views.dog_index, name='dog-index'),
    path('dogs/<int:dog_id>/', views.dog_detail, name='dog-detail'),
    # new route used to create a dog
    path('dogs/create/', views.DogCreate.as_view(), name='dog-create'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dog-update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dog-delete'),
    path(
        'dogs/<int:dog_id>/add-feeding/', 
        views.add_feeding, 
        name='add-feeding'
    ),
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),


]
