from django.urls import path
from .views import ( create_emp,show_emp,update_emp,delete_emp )

urlpatterns = [
    path('create/',create_emp,name='create_emp'),
    path('show/',show_emp,name='show_emp'),
    path('update/<int:pk>/',update_emp,name='update_emp'),
    path('delete/<int:pk>/',delete_emp,name='delete_emp')
]