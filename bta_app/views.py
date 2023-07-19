from django.shortcuts import render
# from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Beat
# from .forms import BeatingForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def beats_index(request):
    beats = Beat.objects.all()
    return render(request, 'beats/index.html', {
        'beats': beats
    })

def beats_detail(request, beat_id):
  beat = Beat.objects.get(id=beat_id)
  return render(request, 'beats/detail.html', { 'beat': beat })

class BeatCreate(CreateView):
    model = Beat
    fields = '__all__'
    success_url = '/beats/{beat_id}'

class BeatUpdate(UpdateView):
  model = Beat
  choices=[(‘male’), (‘female’)] choices=, label=‘gender’
  fields = ['Name', 'Demographic', 'Gender', 'Description']

class BeatDelete(DeleteView):
  model = Beat
  success_url = '/beats'

# def beats_detail(request, beat_id):
#   beat = Beat.objects.get(id=beat_id)
#   beating_form = BeatingForm()
#   return render(request, 'beats/detail.html', {
#     'beat': beat, 'beating_form': beating_form
#   })

# def add_beating(request, beat_id):
#   form = BeatingForm(request.POST)
#   if form.is_valid():
#     new_beating = form.save(commit=False)
#     new_beating.beat_id = beat_id
#     new_beating.save()
#   return redirect('detail', beat_id=beat_id)

# def login(request):
#     return render(request, 'login.html')

# def signup(request):
#     return render(request, 'signup.html')

# def pending(request):
#     return render(request, 'pending.html')

# def completed(request):
#     return render(request, 'completed.html')