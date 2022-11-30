from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from django.urls import reverse_lazy
from .forms import UserCreationFormCustom


# Create your views here.
def home_view(request):
    return render(request, "index.html")

class UserCreateView(CreateView):
    form_class = UserCreationFormCustom
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"