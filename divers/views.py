from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User


# Create your views here.
def home_view(request):
    return render(request, "index.html")

class UserCreateView(CreateView):
    model = User
    success_url = ""
    template_name = "registration/signup.html"