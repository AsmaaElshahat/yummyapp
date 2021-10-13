from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RecipeCreateForm
from .models import Recipe
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def recipe_create(request):
    if request.method == 'POST':
        # form is sent
        form = RecipeCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            # assign current user to the item
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Recipe added successfully')
            # redirect to new created item detail view
            return HttpResponseRedirect(reverse('recipes:list'))
    else:
        # build form with data provided by the bookmarklet via GET
        form = RecipeCreateForm(data=request.GET)
        return render(request, 'recipes/recipe/create.html', {'section': 'recipes', 'form': form})


def recipe_detail(request, id, slug):
    recipe = get_object_or_404(Recipe, id=id, slug=slug)
    return render(request, 'recipes/recipe/detail.html', {'section': 'recipes', 'recipe': recipe})


@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    paginator = Paginator(recipes, 8)
    page = request.GET.get('page')
    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        recipes = paginator.page(1)
    except EmptyPage:
        recipes = paginator.page(paginator.num_pages)
    return render(request, 'recipes/recipe/list.html', {'section': 'recipes', 'recipes': recipes})


def recipe_update(request, id):
    recipe = Recipe.objects.get(id=id)
    form = RecipeCreateForm(instance=recipe)
    if request.method == 'POST':
        form = RecipeCreateForm(data=request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            #return recipe_list(request)
            return HttpResponseRedirect(reverse('recipes:list'))
    context = {'form': form}
    return render(request, 'recipes/recipe/update.html', context)


def recipe_delete(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == 'POST':
        recipe.delete()
        return HttpResponseRedirect(reverse('recipes:list'))
    context = {'recipe': recipe}
    return render(request, 'recipes/recipe/delete.html', context)
