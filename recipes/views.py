from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe
from django.db.models import Q
from django.contrib import messages

from utils.pagination import make_pagination
import os
# Create your views here.

PER_PAGE = int(os.environ.get("PER_PAGE", 6))

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/home.html', context={
        'recipes': page_obj,
        'pagination_range':pagination_range
    })

def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id'))
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)
    return render(request, 'recipes/pages/category.html', context={
        'recipes': page_obj,
        'title': f'{recipes[0].category.name} - Category',
        'pagination_range':pagination_range
    })

def recipes(request, id):
    recipe = get_object_or_404(Recipe, id=id, is_published=True)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_datail_page':True,
    })

def search(request):
    search_term = request.GET.get("q", '').strip()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term)
        ),
        is_published=True
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    if not search_term:
        raise Http404()
    return render(request, 'recipes/pages/search.html', {
        'search_term':search_term,
        'recipes':page_obj,
        'pagination_range':pagination_range,
        'additional_url_query':f'&q={search_term}'
    })