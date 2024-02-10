from django.shortcuts import render
from .models import Entry
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import EntryForm, PhotoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test


def home(request):
    entries = Entry.objects.all().order_by('-date_posted')
    return render(request, 'app/home.html', {'entries': entries})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Opcjonalnie zaloguj użytkownika od razu po rejestracji
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



@login_required
def add_entry(request):
    if request.method == 'POST':
        entry_form = EntryForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)
        if entry_form.is_valid() and photo_form.is_valid():
            entry = entry_form.save(commit=False)
            entry.author = request.user
            entry.save()
            photo = photo_form.save(commit=False)
            photo.entry = entry
            photo.save()
            return redirect('home')
    else:
        entry_form = EntryForm()
        photo_form = PhotoForm()
    return render(request, 'app/add_entry.html', {'entry_form': entry_form, 'photo_form': photo_form})

def is_admin(user):
    return user.is_authenticated and user.is_superuser

@login_required
@user_passes_test(is_admin)
def delete_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    entry.delete()
    return redirect('home')  # Przekierowanie do strony głównej po usunięciu wpisu