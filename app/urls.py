from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include, reverse_lazy
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_entry, name='add_entry'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('entry/delete/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]
