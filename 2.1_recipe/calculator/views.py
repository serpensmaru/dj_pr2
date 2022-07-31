from django.shortcuts import render
from django.shortcuts import render, reverse
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def home(request):
    return HttpResponse(f"Введите название рецепта. Пример ...8000/omlet/")

def get_recipe(request, recipe_data):
    template_name = "calculator/index.html"
    parameter = request.GET.get('servings')
    if parameter is None:
        parameter = 1
    else:
        parameter = int(parameter)
    print(parameter)
    recipe = DATA[recipe_data].copy()
    for key, val in DATA[recipe_data].items():
        recipe[key] = val * parameter
    context = {
        'recipe': recipe,
    }
    return render(request, template_name, context)



