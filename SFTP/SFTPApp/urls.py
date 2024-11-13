from django.urls import path, include
from .views  import home,succesful

urlpatterns = [
    path("", home, name="home"),
    path("succesful", succesful, name="succesful"),
]
