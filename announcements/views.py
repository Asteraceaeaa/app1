from django.shortcuts import render

# Create your views here.

def annoucementsPage(request):
  return render(request, 'main/index.html')