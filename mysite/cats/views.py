from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Cat, Breed
from cats.forms import MakeForm

# Create your views here.

class CatList(LoginRequiredMixin, View) :
    def get(self, request):
        mc = Breed.objects.all().count();
        al = Cat.objects.all();

        ctx = { 'breed_count': mc, 'cat_list': al };
        return render(request, 'cats/cat_list.html', ctx)

class BreedList(LoginRequiredMixin,View) :
    def get(self, request):
        ml = Breed.objects.all();
        ctx = { 'breed_list': ml };
        return render(request, 'cats/breed_list.html', ctx)

class BreedCreate(LoginRequiredMixin,CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

# Take the easy way out on the main table
class CatCreate(LoginRequiredMixin,CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

