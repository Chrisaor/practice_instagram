from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
# Create your views here.
from instagram.forms import CreateUserForm, UploadForm

@login_required
def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit = False)
            photo.owner = request.user
            form.save()
            return redirect('instagram:index')

    form = UploadForm()
    return render(request, 'instagram/upload.html', {'form':form})

class IndexView(TemplateView):
    template_name = 'instagram/index.html'

class CreatUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('create_user_done')

class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'
