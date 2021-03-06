from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.base import TemplateView, View
from django.contrib.auth.decorators import login_required

from instagram.forms import UploadForm, UserForm, ProfileForm


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


class ProfileUpdateView(View):
    def get(self, request):
        pk = request.user.pk
        user = get_object_or_404(User, pk=pk)
        user_form = UserForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
        })
        if hasattr(user, 'profile'):
            profile = user.profile
            profile_form = ProfileForm(initial={
                'nickname': profile.nickname,
                'profile_photo':profile.profile_photo,
            })
        else:
            profile_form = ProfileForm()

        return render(request, 'instagram/profile_update.html', {"user_form":user_form,"profile_form":profile_form})

    def post(self, request):
        pk = request.user.pk
        u = User.objects.get(id=pk)
        user_form = UserForm(request.POST, instance=u)

        if (user_form.is_valid()):
            user_form.save()

            if hasattr(u, 'profile'):
                profile = u.profile
                profile_form = ProfileForm(request.POST, request.FILES,
                                           instance=profile)
            else:
                profile_form = ProfileForm(request.POST, request.FILES)

            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = u
                profile.save()

            return redirect('instagram:profile', pk)


