from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
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


class IndexView(ListView):
    context_object_name = 'user_photo_list'
    paginate_by = 2

    def get_queryset(self):
        user = self.request.user
        return user.photo_set.all().order_by('-pub_date')


class ProfileView(DetailView):
    context_object_name = 'profile_name'
    model = User
    template_name = 'instagram/profile.html'
