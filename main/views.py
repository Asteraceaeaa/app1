from django.shortcuts import render

# Create your views here.


def main(request):
  context = {
    'title': 'Объявления',
    # 'content': 'Страница с объявлениями',
  }


  return render(request, 'main/index.html')