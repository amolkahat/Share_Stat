from django.urls import path
from .views import index, login, signup, contact, about


urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about')
]
