from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm

# Create your views here.

def index(request):
    news = News.objects.all()
    return render(request, 'news/index.html', {'news': news,
                                               'title': 'Список новостей',
                                               })
def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news,
                                               'category': category,
                                               })

def view_news(request, news_id):
    #news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)    #Забираем из формы данные
        if form.is_valid():
            #print(form.cleaned_data)
            News.objects.create(**form.cleaned_data)  # Операция распаковки словаря в Python
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
