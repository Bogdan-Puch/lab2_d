from django.shortcuts import render
def home(request):
    
    context = {'title': 'Головна сторінка', 'is_home': True}
    return render(request, 'superstars/index.html', context)

def star1(request):

    context = {'title': 'Зірка №1', 'is_home': False}
    return render(request, 'superstars/index.html', context)
# Create your views here.
def star2(request):
    context = {'page_title': 'Зірка №2', 'main_text': 'Це опис другої суперзірки.', 'is_home': False}
    return render(request, 'superstars/index.html', context)