from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from django.contrib.auth.forms import AdminPasswordChangeForm
from profiles.forms import ProfileCreationForm, EditProfileForm, AdminEditPasswordForm

# Create your views here.
User = get_user_model()


class ProfileListView(LoginRequiredMixin, ListView):
    model = User

    def get_context_data(self, **kwargs):
        context = super(ProfileListView, self).get_context_data(**kwargs)
        return context


@login_required
def profile_create(request):
    form = ProfileCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/u')

    template_name = 'profiles/user_create.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required
def profile_edit(request, pk):
    user = get_object_or_404(User, id=pk)
    form = EditProfileForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('/u')

    template_name = 'profiles/user_edit.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required
def admin_edit_password(request, pk):
    user = get_object_or_404(User, id=pk)
    form = AdminPasswordChangeForm(user=user)
    if request.method == 'POST':
        form = AdminPasswordChangeForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/u')
    template_name = 'profiles/user_admin_edit_password.html'
    context = {'form': form}
    return render(request, template_name, context)
